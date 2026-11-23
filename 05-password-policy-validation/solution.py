"""
Case Study 29: Password Policy Validation Engine
-------------------------------------------------
Syllabus: strings, string methods, conditional statements, loops,
operators, boolean logic, reporting failures.
"""

PROHIBITED = ["password", "123456", "admin", "qwerty"]
MIN_LENGTH = 8
SPECIALS = "!@#$%^&*()-_=+[]{};:,.<>?"


def has_repetition(pw, run_limit=3):
    """True if any character repeats `run_limit` times consecutively."""
    run = 1
    for i in range(1, len(pw)):
        if pw[i] == pw[i - 1]:
            run += 1
            if run >= run_limit:
                return True
        else:
            run = 1
    return False


def validate(pw):
    """Return a list of failed-condition messages (empty list => valid)."""
    errors = []

    if len(pw) < MIN_LENGTH:
        errors.append("length %d is below minimum %d" % (len(pw), MIN_LENGTH))

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in pw:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True
        elif ch in SPECIALS:
            has_special = True

    if not has_upper:
        errors.append("missing an uppercase letter (A-Z)")
    if not has_lower:
        errors.append("missing a lowercase letter (a-z)")
    if not has_digit:
        errors.append("missing a digit (0-9)")
    if not has_special:
        errors.append("missing a special character (%s)" % SPECIALS[:8] + "...")

    lower = pw.lower()
    for word in PROHIBITED:
        if word in lower:
            errors.append("contains prohibited substring '%s'" % word)

    if has_repetition(pw):
        errors.append("contains 3+ identical characters in a row")

    return errors


def main():
    samples = [
        "welcome",
        "Passw0rd",
        "Strong#Pass1",
        "aaabbbCCC123!",
        "admin@12345",
        "MyCampus#2026",
        "AAAAAAAAaaaa1111!",
    ]

    print("=" * 70)
    print("  PASSWORD POLICY VALIDATION ENGINE")
    print("=" * 70)
    print("Policy: length >= %d, upper+lower+digit+special, no prohibited" % MIN_LENGTH)
    print("substrings %s, no 3-in-a-row repeats." % PROHIBITED)
    print("-" * 70)

    passed = 0
    for pw in samples:
        errors = validate(pw)
        if not errors:
            passed += 1
            print("  [ PASS ] %-20s -> accepted" % pw)
        else:
            print("  [ FAIL ] %-20s -> %d problem(s)" % (pw, len(errors)))
            for e in errors:
                print("            * %s" % e)

    print("-" * 70)
    print("Result: %d of %d sample passwords satisfy the policy."
          % (passed, len(samples)))


if __name__ == "__main__":
    main()
