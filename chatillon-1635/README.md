# Châtillon to Servien on 3 August 1635

Research status as of 5 October 2026: **partial reconstruction; no complete decipherment or uniquely validated key.**

## Research task

Reconstruct the graphical and numerical cipher in Châtillon's letter to Servien from Nijmegen, 3 August 1635, and distinguish genuinely repeatable assignments from fits that depend on uncertain plaintext, sign grouping or output length.

The manuscript is BnF Français 3758, item 104. The letter begins below its heading on the right-hand page of [Gallica view 135](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f135.item) and ends on the left-hand page of [view 140](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f140.item). The royal letter beginning on the opposite page is a different document. Cipher passages occur in views 136, 139 and 140.

This investigation is separate from the [Louis XIII letter of 30 June 1635](https://github.com/Cipher-Atelier/louis-xiii-cipher-letter-june-1635/blob/main/louis-xiii-june-1635/README.md). A statement in Châtillon's letter says that Brézé supplied a cipher previously used by Servien during a German journey. That is historical provenance, not proof that either document uses the June key.

## Tests completed

### Transfer and independent reconstruction

An initial transfer trial used frozen June-letter tables on a preselected 148-group passage. The conservative overlay supplied conditional values at 14 positions, with no independently verified word. This measured coverage, not accuracy, and did not establish a common key.

A separate ciphertext-only attack used Châtillon's material without June-key values. Its solver produced no stable reading. Promising development-control results failed to generalize to fresh controls; a subsequent normalized language-model candidate also failed its development gate. Those results do not support treating either solver as a validated decipherer of the manuscript.

Source-aided reconstruction then compared cipher blocks with detached clear notes in the same manuscript. It produced a 21-entry conditional table and some meaningful bounded sequences, but retained conflicting sign values, word-order differences and uncertain correspondence between the complete passages. These were exposed-text diagnostics, not new blind trials.

### A conditional repeat-sign result

A delta-like sign was tested as an instruction to repeat either the preceding character or the preceding resolved unit. The idea was developed after seeing earlier patterns. A later prediction was registered before a newly obtained clear note was inspected.

In that later check, both the predecessor and the putative repeat sign were masked independently. A bounded alignment of the first 15 cipher groups forced two successive normalized u characters in the source word *trouué*. The two spellings considered farther down the note gave the same local result. They were sensitivity variants, not independent confirmations.

The complete continuation failed: 41 positive-length cipher groups could not fit the proposed 39- or 40-letter counterpart. Repeating one character and repeating the whole preceding unit remain indistinguishable in the successful local example. A further test of consistent null assignments found no surviving explanation within its declared family. The local result therefore supports one conditional prediction, not a global operator or a complete reading.

### The latest dependency test

A later visual review distinguished two open and two closed examples of another crossed sign. Proposed values failed to transfer consistently between the available contexts. The 5 October test asked which inherited assumptions forced the closed form to f.

All 512 subsets of nine active inherited assignments were evaluated in 12 recorded source/grouping conditions, giving 6,144 conditions. The 12 branches contain six distinct alignment problems because two spelling alternatives differ beyond every reachable endpoint. Independent enumerators reproduced the recorded counts.

The decisive contrast concerned the neighboring numeral labelled N2:

- With the other eight inherited mappings retained, allowing N2 to be any single letter still forced the closed sign to f. N2 itself could be d or r.
- Allowing N2 to consume one to eight letters admitted e, f, n or r at the closed sign.
- This relaxation still did not admit s there, so it did not reconcile the earlier conflicting transfer window.

The result identifies a dependency on a numerical output-length assumption. It does not prove that N2 means r, that one letter is the only sufficient possible bound, or that any alternative is historically correct. Removed assignments became independent alignment slots, so this was not an enumeration of coherent complete keys.

## What remains unresolved

- Whether the detached notes are exact counterparts of the complete cipher passages
- The grouping, value and output length of N2
- Which graphical distinctions are cryptographic rather than handwriting variation
- The scope and exact semantics of the proposed repeat sign
- A key that explains all occurrences without selective spelling or boundary repairs

The most discriminating next evidence is a securely bounded same-key occurrence establishing N2's output length, an independent literal plaintext witness, or a contemporary key. Further enlargement alone cannot establish semantic value.

## Sources and earlier work

- [BnF Français 3758, view 137](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f137.item): the letter's statement about Brézé and the earlier cipher.
- [View 138](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f138.item), [view 139](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f139.item) and [view 140](https://gallica.bnf.fr/ark:/12148/btv1b9058223v/f140.item): clear notes, cipher blocks and letter boundaries.
- Daniel Bourdeau, [Rohan papers and the Franco-Dutch letters, 1635–36](https://dbourdeau.github.io/cyphersolver/rohan1636.html): credited for the modern source lead and correspondence context.
- Antoine Aubery, *Mémoires pour l'histoire du cardinal duc de Richelieu*, volume I, 1660: an earlier printed-source lead, with candidate pages 509–510 in the research record. The exact recipient heading and image-backed wording of that candidate passage remain unverified here. Related text is already known from historical publication; this investigation makes no claim of first discovery or first publication.

Manuscript preservation and digitization are credited to the Bibliothèque nationale de France. The contribution described here is a sequence of conditional reconstructions, failed transfer tests and model-dependency checks.

## Documentation note

This research summary was prepared with AI assistance.

[Back to the research catalogue](../README.md)
