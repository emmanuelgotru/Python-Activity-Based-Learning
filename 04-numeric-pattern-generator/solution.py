"""
Case Study 27: Advanced Numeric Pattern Generator
--------------------------------------------------
Syllabus: nested loops, conditional statements, operators, pattern
generation, input validation, string formatting.
"""


def hollow_diamond(n):
    """Print a hollow diamond of height n (must be odd, >= 3)."""
    if n < 3 or n % 2 == 0:
        print("  INVALID: size %d -> must be an odd integer >= 3." % n)
        return False

    mid = n // 2
    for i in range(n):
        dist = abs(i - mid)
        digit = str(mid - dist + 1)
        row_len = 2 * (mid - dist) + 1
        pad = (n - row_len) // 2
        line = ""
        for j in range(row_len):
            if j == 0 or j == row_len - 1:
                line += digit
            else:
                line += " "
        print(" " * pad + line)
    return True


def number_pyramid(m):
    """Print a symmetric numeric pyramid of height m (must be >= 1)."""
    if m < 1:
        print("  INVALID: size %d -> must be >= 1." % m)
        return False
    for i in range(1, m + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        for j in range(i - 1, 0, -1):
            line += str(j)
        print(" " * (m - i) + line)
    return True


def main():
    print("=" * 46)
    print("  ADVANCED NUMERIC PATTERN GENERATOR")
    print("=" * 46)

    print("\nPATTERN 1: Hollow diamond, size 5")
    print("-" * 46)
    hollow_diamond(5)

    print("\nPATTERN 1: Hollow diamond, size 7")
    print("-" * 46)
    hollow_diamond(7)

    print("\nPATTERN 1: Validation check (even size 6)")
    print("-" * 46)
    hollow_diamond(6)

    print("\nPATTERN 1: Validation check (size 1)")
    print("-" * 46)
    hollow_diamond(1)

    print("\nPATTERN 2: Symmetric number pyramid, size 4")
    print("-" * 46)
    number_pyramid(4)

    print("\nPATTERN 2: Validation check (size -3)")
    print("-" * 46)
    number_pyramid(-3)

    print("\nDone. All dimensions validated before printing.")


if __name__ == "__main__":
    main()
