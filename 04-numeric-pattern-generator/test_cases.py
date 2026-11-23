"""Automated test cases for Case Study 27 - Advanced Numeric Pattern Generator."""
import importlib.util
import io
import os
from contextlib import redirect_stdout

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


def capture(func, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        result = func(*args)
    return result, buf.getvalue().strip("\n")


# TC-01: valid odd size accepted
ok, out = capture(sol.hollow_diamond, 5)
check("size 5 accepted", ok is True)

# TC-02: hollow diamond prints exactly 5 rows
check("5 rows printed", len(out.splitlines()) == 5)

# TC-03: centre row of size 5 is '3   3' (hollow)
centre = out.splitlines()[2]
check("centre row hollow: '3   3'", centre.strip() == "3   3")

# TC-04: even size rejected
ok, out = capture(sol.hollow_diamond, 6)
check("even size 6 rejected", ok is False and "INVALID" in out)

# TC-05: size below 3 rejected
ok, out = capture(sol.hollow_diamond, 1)
check("size 1 rejected", ok is False and "INVALID" in out)

# TC-06: pyramid of size 4 accepted and symmetric
ok, out = capture(sol.number_pyramid, 4)
lines = out.splitlines()
check("pyramid size 4 accepted", ok is True and len(lines) == 4)
check("last pyramid row is 1234321", lines[-1] == "1234321")

# TC-07: negative pyramid size rejected
ok, out = capture(sol.number_pyramid, -3)
check("negative size rejected", ok is False and "INVALID" in out)

# TC-08: first row of pyramid is centred single '1'
check("pyramid top row is '1'", lines[0] == "   1")

print("\nALL %d TESTS PASSED (Case Study 27)" % passed)
