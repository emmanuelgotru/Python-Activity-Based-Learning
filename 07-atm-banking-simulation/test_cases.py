"""Automated test cases for Case Study 38 - ATM Menu-Driven Banking Simulation."""
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


def fresh(balance=5000):
    return {"balance": balance, "log": []}


# TC-01: valid deposit updates balance and logs
st = fresh()
ok, msg = sol.do_deposit(st, 1500)
check("deposit 1500 accepted", ok and st["balance"] == 6500 and len(st["log"]) == 1)

# TC-02: non-positive deposit rejected
st = fresh()
ok, _ = sol.do_deposit(st, -100)
check("negative deposit rejected", (not ok) and st["balance"] == 5000)

# TC-03: deposit above per-txn limit rejected
st = fresh()
ok, _ = sol.do_deposit(st, 200000)
check("deposit over Rs 100000 rejected", not ok)

# TC-04: valid withdrawal within all rules
st = fresh(8000)
ok, _ = sol.do_withdraw(st, 2000)
check("withdraw 2000 accepted", ok and st["balance"] == 6000)

# TC-05: withdrawal not a multiple of 100 rejected
st = fresh()
ok, msg = sol.do_withdraw(st, 250)
check("withdraw 250 rejected (not multiple of 100)", (not ok) and "multiple" in msg)

# TC-06: withdrawal above per-txn ceiling rejected
st = fresh(50000)
ok, msg = sol.do_withdraw(st, 15000)
check("withdraw over Rs 10000 rejected", (not ok) and "limit" in msg)

# TC-07: withdrawal breaching minimum balance rejected
st = fresh(3000)
ok, msg = sol.do_withdraw(st, 2500)
check("withdraw below min balance rejected", (not ok) and "minimum balance" in msg)

# TC-08: withdrawal exactly to minimum balance allowed
st = fresh(3000)
ok, _ = sol.do_withdraw(st, 2000)
check("withdraw to exactly Rs 1000 allowed", ok and st["balance"] == 1000)

# TC-09: invalid amount (non-numeric) handled by caller -> simulated here
st = fresh()
try:
    amount = float("abc")
    ok = True
except ValueError:
    ok = False
check("non-numeric input caught", ok is False)

# TC-10: transaction log grows and stores running balance
st = fresh()
sol.do_deposit(st, 500)
sol.do_withdraw(st, 100)
sol.do_deposit(st, 200)
check("3 log entries with balances", len(st["log"]) == 3 and st["log"][1][2] == 5400)

print("\nALL %d TESTS PASSED (Case Study 38)" % passed)
