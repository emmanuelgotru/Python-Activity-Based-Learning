"""Automated test cases for Case Study 26 - Nested Loop Seating Generator."""
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


seat = sol.build_seating()

# TC-01: grid dimensions
check("grid has 6 rows", len(seat) == 6)
check("every row has 8 columns", all(len(r) == 8 for r in seat))

# TC-02: reserved seats marked R
check("(2,3) is reserved", seat[1][2] == "R")
check("(5,7) is reserved", seat[4][6] == "R")

# TC-03: alternate-spacing rule blocks odd columns in rows 2,4,6
check("(2,1) blocked by alternate rule", seat[0][0] == "O" and seat[1][0] == "X")
check("(4,5) blocked", seat[3][4] == "X")
check("even columns stay open in row 2", seat[1][1] == "O")

# TC-04: reserved seats win over alternate blocking
check("(2,3) reserved even though odd column", seat[1][2] == "R")

# TC-05: default reserved list passes validation
check("default RESERVED list is valid", sol.validate_reserved() == [])

# TC-06: out-of-range reserved seat detected
old = sol.RESERVED[:]
sol.validate_reserved.__globals__["RESERVED"] = [(9, 2)]
problems = sol.validate_reserved()
sol.validate_reserved.__globals__["RESERVED"] = old
check("out-of-range seat (9,2) flagged", len(problems) == 1 and "outside" in problems[0])

# TC-07: seat counts add up to full grid
o, r, x = sol.count_seats(seat)
check("O + R + X = 48", o + r + x == 48)
check("3 reserved seats", r == 3)

print("\nALL %d TESTS PASSED (Case Study 26)" % passed)
