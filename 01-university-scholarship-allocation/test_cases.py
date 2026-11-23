"""Automated test cases for Case Study 01 - University Scholarship Allocation."""
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


# TC-01: eligible applicant passes all criteria
ok, agg, reasons = sol.evaluate(sol.APPLICANTS[0])          # S101 Ananya
check("S101 eligible with aggregate 80.8", ok and abs(agg - 80.8) < 0.01 and reasons == [])

# TC-02: aggregate below threshold is rejected
ok, agg, reasons = sol.evaluate(sol.APPLICANTS[1])          # S102 Bharat
check("S102 rejected: aggregate 58.6 < 60", (not ok) and abs(agg - 58.6) < 0.01)

# TC-03: subject-wise minimum violation reported
ok, _, reasons = sol.evaluate(sol.APPLICANTS[1])
check("S102 subject violation reported", any("Physics" in r for r in reasons))

# TC-04: income criterion violation
ok, _, reasons = sol.evaluate(sol.APPLICANTS[2])            # S103 income 610000
check("S103 rejected: income above limit", (not ok) and any("income" in r for r in reasons))

# TC-05: attendance criterion violation
ok, _, reasons = sol.evaluate(sol.APPLICANTS[5])            # S106 attendance 71
check("S106 rejected: attendance below 75%", (not ok) and any("attendance" in r for r in reasons))

# TC-06: ranking places highest aggregate first
eligible = []
for a in sol.APPLICANTS:
    ok, agg, _ = sol.evaluate(a)
    if ok:
        eligible.append((a[0], a[1], round(agg, 2), a[3], a[4]))
eligible.sort(key=sol.rank_key)
check("S105 Fatima ranked #1", eligible[0][0] == "S105")

# TC-07: tie on aggregate broken by attendance (S108 88% beats S104 76%)
r108 = [i for i in range(len(eligible)) if eligible[i][0] == "S108"][0]
r104 = [i for i in range(len(eligible)) if eligible[i][0] == "S104"][0]
check("tie S108 vs S104 resolved by attendance", eligible[r108][2] == eligible[r104][2] and r108 < r104)

# TC-08: totals
ok_count = sum(1 for a in sol.APPLICANTS if sol.evaluate(a)[0])
check("4 eligible / 4 rejected of 8", ok_count == 4 and len(sol.APPLICANTS) - ok_count == 4)

print("\nALL %d TESTS PASSED (Case Study 01)" % passed)
