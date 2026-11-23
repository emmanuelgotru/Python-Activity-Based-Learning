"""
Case Study 35: Text Compression Using Character Runs (RLE)
-----------------------------------------------------------
Syllabus: strings, loops, conditional statements, operators,
lists, length comparisons.
Assumption: input strings contain letters only (no digits), so the
count part of the encoding is never ambiguous.
"""


def encode(text):
    """Run-length encode: consecutive runs become <char><count>."""
    if text == "":
        return ""
    parts = []
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            parts.append(text[i - 1] + str(count))
            count = 1
    parts.append(text[-1] + str(count))
    return "".join(parts)


def main():
    samples = [
        "aaabbbcccdddd",
        "python",
        "aaaaaaaaaaaaaaaaaaaa",
        "compression",
        "zzzzzzzzzzzzzzzzzzzzzzzzzzzz",
        "mississippi",
        "",
    ]

    print("=" * 78)
    print("  TEXT COMPRESSION USING CHARACTER RUNS (Run-Length Encoding)")
    print("=" * 78)
    print("%-30s %7s   %-30s %7s  %s" %
          ("Original", "Len", "Encoded", "Len", "Verdict"))
    print("-" * 78)

    beneficial = 0
    for s in samples:
        enc = encode(s)
        if len(enc) < len(s):
            verdict = "compressed by %d bytes" % (len(s) - len(enc))
            beneficial += 1
        elif len(enc) > len(s):
            verdict = "NOT beneficial (+%d bytes)" % (len(enc) - len(s))
        else:
            verdict = "same length - not beneficial"
        print("%-30s %7d   %-30s %7d  %s" %
              (s if s else "(empty)", len(s), enc if enc else "(empty)", len(enc), verdict))

    print("-" * 78)
    print("Compression was beneficial for %d of %d samples." %
          (beneficial, len(samples)))
    print("Note: highly repetitive text compresses well; random or short")
    print("text usually grows, because counts add extra characters.")


if __name__ == "__main__":
    main()
