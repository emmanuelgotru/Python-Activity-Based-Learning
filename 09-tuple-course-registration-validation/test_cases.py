"""Automated test cases for Case Study 64 - Tuple-Based Course Registration Validation."""
import importlib.util
import os

spec = importlib.util.spec_from_file_location(
    "sol", os.path.join(os.path.dirname(__file__), "solution.py"))
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)

passed = 0


def check(label, condition):
    global passed
    assert condition, "FAILED: " + label
    passed += 1
    print("  PASS:", label)


by_roll = {s[0]: s for s in sol.REGISTRATIONS}

# TC-01: clean registration passes
check("R01 valid", sol.validate(by_roll["R01"]) == [])

# TC-02: duplicate course code detected
v = sol.validate(by_roll["R02"])
check("R02 duplicate CS101 detected", any("duplicate" in x for x in v))

# TC-03: missing prerequisite detected
v = sol.validate(by_roll["R03"])
check("R03 missing prerequisite CS101", any("prerequisite" in x and "CS101" in x for x in v))

# TC-04: mutually exclusive pair detected
v = sol.validate(by_roll["R04"])
check("R04 exclusive pair PHY101+PHY102", any("mutually exclusive" in x for x in v))

# TC-05: over-enrolment (6 > 5) detected
v = sol.validate(by_roll["R04"])
check("R04 exceeds max courses", any("max 5" in x for x in v))

# TC-06: duplicate in R04 also reported
v = sol.validate(by_roll["R04"])
check("R04 duplicate also reported", any("duplicate" in x for x in v))

# TC-07: fully valid 5-course registration
check("R05 valid", sol.validate(by_roll["R05"]) == [])

# TC-08: chained prerequisite failure (CS301 needs CS201)
v = sol.validate(by_roll["R06"])
check("R06 missing CS201 for CS301", any("CS201" in x and "CS301" in x for x in v))

# TC-09: records are tuples with nested tuples of pairs
s = by_roll["R01"]
check("record structure is tuple", isinstance(s, tuple) and isinstance(s[2], tuple))
check("inner items are 2-tuples", all(isinstance(c, tuple) and len(c) == 2 for c in s[2]))

# TC-10: overall tallies - 2 valid, 4 invalid
valid = sum(1 for s in sol.REGISTRATIONS if sol.validate(s) == [])
check("2 valid / 4 invalid of 6", valid == 2 and len(sol.REGISTRATIONS) - valid == 4)

print("\nALL %d TESTS PASSED (Case Study 64)" % passed)
