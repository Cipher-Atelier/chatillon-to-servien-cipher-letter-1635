#!/usr/bin/env python3
"""Scoped offline replay; preserve assertions and original expected values."""
from collections import Counter, defaultdict
from pathlib import Path
import hashlib, json, sys
ROOT=Path(__file__).resolve().parent
if sys.flags.optimize:
    raise SystemExit("Run normal Python; assertion checks must remain enabled.")

def load(topic, name):
    return json.loads((ROOT / topic / name).read_text(encoding='utf-8'))

def digest_table(value):
    raw = json.dumps(value, sort_keys=True, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()

def alignment_counts(tokens, reference, fixed, targets, n2_width=None):
    """Count paths in the position DAG; then project labels through each edge.

    Unmapped occurrences have independent widths. This is not key induction.
    All final endpoints are allowed, as in the archived prefix-alignment test.
    """
    length = len(reference)
    transitions = []
    for token in tokens:
        value = None if token['mapping_masked'] else fixed.get(token['shape'])
        widths = [len(value)] if value is not None else token['widths']
        if value is None and token['shape'] == 'N2' and n2_width is not None:
            widths = list(range(1, n2_width + 1))
        edges = []
        for start in range(length + 1):
            choices = []
            for width in widths:
                end = start + width
                if end <= length and (value is None or reference[start:end] == value):
                    choices.append(end)
            edges.append(choices)
        transitions.append(edges)
    prefix = [{0: 1}]
    for edges in transitions:
        nxt = defaultdict(int)
        for start, count in prefix[-1].items():
            for end in edges[start]:
                nxt[end] += count
        prefix.append(dict(nxt))
    suffix = [[0] * (length + 1) for _ in range(len(tokens) + 1)]
    suffix[-1] = [1] * (length + 1)
    for i in range(len(tokens) - 1, -1, -1):
        for start, ends in enumerate(transitions[i]):
            suffix[i][start] = sum(suffix[i + 1][end] for end in ends)
    projected = []
    for identifier in targets:
        i = next(i for i, token in enumerate(tokens) if token['id'] == identifier)
        counts = Counter()
        for start, before in prefix[i].items():
            for end in transitions[i][start]:
                ways = before * suffix[i + 1][end]
                if ways:
                    counts[reference[start:end]] += ways
        projected.append(dict(counts))
    return sum(prefix[-1].values()), projected, {str(k): v for k, v in prefix[-1].items()}

def check_chatillon():
    data = load('chatillon-1635', 'config.json')
    names = sorted(data['active_mapping'])
    table = []
    forced = 0
    for mask in range(2 ** len(names)):
        fixed = {name: data['active_mapping'][name] for i, name in enumerate(names)
                 if mask & (1 << i)}
        closed_union = set()
        for scenario in data['scenarios']:
            count, projections, _ = alignment_counts(
                scenario['tokens'], scenario['reference'], fixed, data['targets'])
            table.append({'mask': mask, 'reference_id': scenario['reference_id'],
                          'grouping_id': scenario['grouping_id'], 'count': count,
                          'open': projections[0], 'closed': projections[1]})
            closed_union.update(projections[1])
        forced += closed_union == {'f'}
    assert len(table) == data['expected_condition_count']
    assert digest_table(table) == data['expected_ablation_table_sha256']
    assert forced == data['expected_forcing_subsets']
    fixed = {k: v for k, v in data['active_mapping'].items() if k != 'N2'}
    expected = {(r['reference_id'], r['grouping_id'], r['width']): r
                for r in data['expected_width_results']}
    unions = {}
    for width in (1, 8):
        union = set()
        for scenario in data['scenarios']:
            targets = data['targets'] + [t['id'] for t in scenario['tokens'] if t['shape'] == 'N2']
            count, projections, ends = alignment_counts(
                scenario['tokens'], scenario['reference'], fixed, targets, width)
            old = expected[(scenario['reference_id'], scenario['grouping_id'], width)]
            assert (count, projections, ends) == (old['count'], old['projections'], old['end_positions'])
            union.update(projections[1])
        unions[str(width)] = sorted(union)
    return {'status': 'passed', 'ablation_conditions': len(table),
            'width_conditions': len(expected), 'forcing_subsets': forced,
            'closed_values_by_n2_max_width': unions,
            'scope': 'Conditional exposed-text alignment, not a recovered complete key'}

if __name__ == "__main__":
    print(json.dumps({'chatillon-1635': check_chatillon()}, ensure_ascii=False, indent=2))
