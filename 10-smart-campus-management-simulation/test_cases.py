"""Automated test cases for Case Study 100 - Smart Campus Management Simulation."""
import importlib.util
import io
import os
from contextlib import redirect_stdout
from unittest import mock

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


def reset():
    sol.students.clear()
    sol.attendance.clear()
    sol.marks_records.clear()
    sol.event_regs.clear()
    sol.route_stats.clear()


def run_with_input(func, answers):
    buf = io.StringIO()
    with mock.patch("builtins.input", side_effect=answers):
        with redirect_stdout(buf):
            func()
    return buf.getvalue()


reset()

# TC-01: add a valid student
run_with_input(sol.add_student, ["A1", "Ananya", "CSE"])
check("student A1 added", sol.students == [("A1", "Ananya", "CSE")])

# TC-02: duplicate roll rejected
run_with_input(sol.add_student, ["A1", "Clone", "ECE"])
check("duplicate roll rejected", len(sol.students) == 1)

# TC-03: empty roll rejected
run_with_input(sol.add_student, ["", "NoRoll", "ECE"])
check("empty roll rejected", len(sol.students) == 1)

# TC-04: valid attendance recorded, eligibility computed
out = run_with_input(sol.record_attendance, ["A1", "18", "20"])
check("attendance 18/20 = 90% eligible", "90.0%" in out and "ELIGIBLE" in out
      and sol.attendance[0] == ("A1", 18, 20))

# TC-05: attendance below 75% flagged
out = run_with_input(sol.record_attendance, ["A1", "13", "20"])
check("attendance 65% not eligible", "65.0%" in out and "NOT ELIGIBLE" in out)

# TC-06: invalid attendance (present > total) rejected
run_with_input(sol.record_attendance, ["A1", "25", "20"])
check("present > total rejected", len(sol.attendance) == 2)

# TC-07: marks accepted and graded FIRST
out = run_with_input(sol.record_marks, ["A1", "85 78 90 82"])
check("avg 83.75 recorded", "avg=83.75" in out)
check("grade FIRST (avg >= 75)", "grade=FIRST" in out)

# TC-08: marks out of range rejected
run_with_input(sol.record_marks, ["A1", "101 50 60 70"])
check("mark > 100 rejected", len(sol.marks_records) == 1)

# TC-09: event registration and revenue
out = run_with_input(sol.register_event, ["A1", "1"])
check("TechFest registered (Rs 200)", "TechFest" in out and sol.event_regs[0][2] == 200)

# TC-10: duplicate event registration rejected
run_with_input(sol.register_event, ["A1", "1"])
check("duplicate event registration rejected", len(sol.event_regs) == 1)

# TC-11: transport allocation with unserved passengers
out = run_with_input(sol.allocate_transport, ["R1", "180", "40", "4"])
check("R1: 4 buses x 40 = 160 served, 20 unserved", "unserved=20" in out)

# TC-12: summary runs without error and reports totals
out = run_with_input(sol.summary, [])
check("summary reports 1 student", "Students on roll : 1" in out)
check("summary reports revenue Rs 200", "revenue Rs 200" in out)

# TC-13: find_student lookup
check("find_student finds A1", sol.find_student("A1")[1] == "Ananya")
check("find_student misses Z9", sol.find_student("Z9") is None)

reset()
print("\nALL %d TESTS PASSED (Case Study 100)" % passed)
