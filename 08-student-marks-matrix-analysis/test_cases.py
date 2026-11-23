"""Automated test cases for Case Study 42 - Student Marks Matrix Analysis."""
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


M = sol.MARKS

# TC-01: matrix shape 5 students x 5 subjects
check("5 x 5 matrix", len(M) == 5 and all(len(r) == 5 for r in M))

# TC-02: row-wise totals
check("Ananya total = 404", sum(M[0]) == 404)
check("Fatima total = 456", sum(M[4]) == 456)

# TC-03: column averages (Maths = 363/5 = 72.6)
maths_avg = sum(M[r][0] for r in range(5)) / 5
check("Maths average = 72.6", abs(maths_avg - 72.6) < 1e-9)

# TC-04: Physics average 67.6 flagged as weak (< 70)
phys_avg = sum(M[r][1] for r in range(5)) / 5
check("Physics average = 67.6 (weak)", abs(phys_avg - 67.6) < 1e-9 and phys_avg < sol.WEAK_SUBJECT_AVERAGE)

# TC-05: no other subject below weak threshold
avgs = [sum(M[r][c] for r in range(5)) / 5 for c in range(5)]
weak = [sol.SUBJECTS[c] for c in range(5) if avgs[c] < sol.WEAK_SUBJECT_AVERAGE]
check("only Physics is weak", weak == ["Physics"])

# TC-06: top performer is Fatima (highest total)
totals = [sum(M[r]) for r in range(5)]
check("top performer = Fatima", sol.STUDENTS[totals.index(max(totals))] == "Fatima")

# TC-07: lowest single mark 48 (Bharat, Physics)
low = min(min(row) for row in M)
check("lowest mark = 48", low == 48)

# TC-08: at-risk student (avg < 60) is Bharat
avgs_students = [sum(M[r]) / 5 for r in range(5)]
at_risk = [sol.STUDENTS[r] for r in range(5) if avgs_students[r] < sol.AT_RISK_AVERAGE]
check("only Bharat at risk", at_risk == ["Bharat"])

# TC-09: grade boundaries
check("avg 90 -> A", sol.grade_of(90) == "A (Distinction)")
check("avg 75 -> B", sol.grade_of(75) == "B (First Class)")
check("avg 60 -> C", sol.grade_of(60) == "C (Second Class)")
check("avg 40 -> D", sol.grade_of(40) == "D (Third Class)")

# TC-10: all marks within 0-100
check("all marks within 0-100", all(0 <= m <= 100 for row in M for m in row))

print("\nALL %d TESTS PASSED (Case Study 42)" % passed)
