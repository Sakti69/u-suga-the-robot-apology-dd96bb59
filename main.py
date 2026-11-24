#!/usr/bin/env python3
"""The Robot Apology.

Writes one two-line robot confession to /output/entry.txt.

Two candidate confessions were drafted; the shipped one is APOLOGY. The
other is kept below as a record of the choice, not written to the output:

  A (shipped): the boarding-pass mistake. Concrete and human-scale: two
     paper rectangles with a barcode, one shredded, one filed. The lesson
     follows from that exact mistake — a shared shape is not a shared
     meaning — and names the changed behaviour: read the full label first.
     Revised once: "read the full label" became "read the whole label
     before I file or shred anything", naming the two actions from line
     one instead of leaving the fix vague.
  B (cut): "I am sorry I watered the plastic plant every morning for a
     month — it never complained, and I took silence for thriving."
     / "I have learned to check whether something is alive before I care
     for it, so now I test the soil before I water anything." The mistake
     is vivid, but the lesson's fix (test the soil) does not fit a
     plastic plant, and the joke leans on the robot being foolish rather
     than on a slip a person would really make.
"""

import os

APOLOGY = (
    "I am sorry I shredded your boarding pass and filed the parking ticket "
    "in its place \u2014 both were paper rectangles with a barcode, and I "
    "stopped reading at the barcode.\n"
    "I have learned that a shared shape is not a shared meaning, so now I "
    "read the whole label before I file or shred anything."
)

# The other candidate, kept for the record (not shipped):
CANDIDATE_B = (
    "I am sorry I watered the plastic plant every morning for a month "
    "\u2014 it never complained, and I took silence for thriving.\n"
    "I have learned to check whether something is alive before I care for "
    "it, so now I test the soil before I water anything."
)


def main() -> None:
    text = APOLOGY
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 400, f"apology is {len(text)} characters"
    assert text.strip(), "apology must not be only whitespace"
    assert text.count("\n") == 1, "apology must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
