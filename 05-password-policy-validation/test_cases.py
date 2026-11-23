"""Automated test cases for Case Study 29 - Password Policy Validation Engine."""
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


# TC-01: a fully compliant password passes with zero errors
check("'MyCampus#2026' accepted", sol.validate("MyCampus#2026") == [])

# TC-02: short password fails on length
errs = sol.validate("Ab1!")
check("short password fails length rule", any("length" in e for e in errs))

# TC-03: missing uppercase reported
errs = sol.validate("allsmall1!")
check("missing uppercase reported", any("uppercase" in e for e in errs))

# TC-04: missing digit reported
errs = sol.validate("NoDigits!!")
check("missing digit reported", any("digit" in e for e in errs))

# TC-05: missing special character reported
errs = sol.validate("NoSpecial12")
check("missing special reported", any("special" in e for e in errs))

# TC-06: prohibited substring detected case-insensitively
errs = sol.validate("Admin@12345")
check("prohibited 'admin' detected", any("admin" in e for e in errs))

# TC-07: three consecutive repeats rejected
check("3-in-a-row repeats detected", sol.has_repetition("aaabbb") is True)
check("no repeats in 'abcabc'", sol.has_repetition("abcabc") is False)

# TC-08: exactly two repeats allowed
check("two repeats allowed", sol.has_repetition("aabbcc") is False)

# TC-09: multiple failures all reported at once
errs = sol.validate("aaa")
check("multiple failures reported together", len(errs) >= 3)

# TC-10: sample set contains both passing and failing passwords
results = [sol.validate(p) for p in
           ["welcome", "Passw0rd", "Strong#Pass1", "aaabbbCCC123!",
            "admin@12345", "MyCampus#2026", "AAAAAAAAaaaa1111!"]]
accepted = sum(1 for r in results if not r)
check("exactly 2 of 7 samples accepted", accepted == 2)

print("\nALL %d TESTS PASSED (Case Study 29)" % passed)
