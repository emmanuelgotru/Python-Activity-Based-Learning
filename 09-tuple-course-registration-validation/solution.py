"""
Case Study 64: Tuple-Based Course Registration Validation
---------------------------------------------------------
Syllabus: tuples, tuple operations, tuple unpacking, nested tuples,
lists, conditional statements, loops, duplicate detection.
"""

MAX_COURSES = 5
PREREQ = {"CS201": "CS101", "CS301": "CS201"}     # course -> required course
MUTUALLY_EXCLUSIVE = [("PHY101", "PHY102")]       # pick only one

# (roll, name, ((code, title), ...))
REGISTRATIONS = [
    ("R01", "Ananya", (
        ("CS101", "Intro to Programming"),
        ("MATH101", "Calculus"),
        ("PHY101", "Physics I"),
    )),
    ("R02", "Bharat", (
        ("CS101", "Intro to Programming"),
        ("CS101", "Intro to Programming"),       # duplicate
        ("CS201", "Data Structures"),
    )),
    ("R03", "Chitra", (
        ("CS201", "Data Structures"),            # missing prerequisite CS101
        ("MATH101", "Calculus"),
    )),
    ("R04", "Deepak", (
        ("CS101", "Intro to Programming"),
        ("PHY101", "Physics I"),
        ("PHY102", "Physics II"),                # exclusive pair
        ("MATH101", "Calculus"),
        ("CS101", "Intro to Programming"),       # duplicate + 6th course
        ("ENG101", "Technical English"),
    )),
    ("R05", "Fatima", (
        ("CS101", "Intro to Programming"),
        ("CS201", "Data Structures"),
        ("MATH101", "Calculus"),
        ("PHY101", "Physics I"),
        ("ENG101", "Technical English"),
    )),
    ("R06", "Gopal", (
        ("CS301", "Algorithms"),                 # missing CS201 (and CS101)
        ("MATH101", "Calculus"),
    )),
]


def validate(student):
    """Return list of rule violations for one registration tuple."""
    roll, name, courses = student          # tuple unpacking
    codes = []
    for code, title in courses:            # unpacking each inner tuple
        codes.append(code)

    violations = []

    # rule 1: no duplicate course codes
    for c in codes:
        if codes.count(c) > 1 and ("duplicate '%s'" % c) not in violations:
            violations.append("duplicate '%s'" % c)

    # rule 2: at most MAX_COURSES courses
    if len(courses) > MAX_COURSES:
        violations.append("enrolled in %d courses (max %d)" % (len(courses), MAX_COURSES))

    # rule 3: prerequisites must also be registered
    for c in codes:
        if c in PREREQ and PREREQ[c] not in codes:
            msg = "missing prerequisite %s for %s" % (PREREQ[c], c)
            if msg not in violations:
                violations.append(msg)

    # rule 4: mutually exclusive pairs
    for a, b in MUTUALLY_EXCLUSIVE:
        if a in codes and b in codes:
            violations.append("mutually exclusive pair %s + %s" % (a, b))

    # rule 5: every course code must be a known code
    known = {"CS101", "CS201", "CS301", "MATH101", "PHY101", "PHY102", "ENG101"}
    for c in codes:
        if c not in known:
            violations.append("unknown course code '%s'" % c)

    return violations


def main():
    print("=" * 74)
    print("  TUPLE-BASED COURSE REGISTRATION VALIDATION")
    print("=" * 74)
    print("Rules: max %d courses, no duplicates, prerequisites satisfied," % MAX_COURSES)
    print("exclusive pairs not combined, only known course codes.")
    print("-" * 74)

    violators = []
    for student in REGISTRATIONS:
        roll, name, courses = student
        codes = [c for c, t in courses]
        violations = validate(student)
        status = "VALID" if not violations else "INVALID"
        print("  %s (%s) - %d course(s): %s"
              % (roll, name, len(courses), ", ".join(codes)))
        print("      -> %s" % status)
        for v in violations:
            print("         * %s" % v)
        if violations:
            violators.append((roll, name))

    print("-" * 74)
    print("Summary: %d valid, %d violating student(s)."
          % (len(REGISTRATIONS) - len(violators), len(violators)))
    if violators:
        print("Students violating rules:")
        for roll, name in violators:
            print("   - %s %s" % (roll, name))


if __name__ == "__main__":
    main()
