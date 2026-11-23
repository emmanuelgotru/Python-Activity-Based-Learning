"""Automated test cases for Case Study 02 - Progressive Electricity Billing."""
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


# TC-01: first slab only (0-100 @ 5)
check("slab_charge(100) = 500", sol.slab_charge(100) == 500.0)

# TC-02: two slabs (100@5 + 200@7 = 1900)
check("slab_charge(300) = 1900", sol.slab_charge(300) == 1900.0)

# TC-03: three slabs (1900 + 200@9 = 3700)
check("slab_charge(500) = 3700", sol.slab_charge(500) == 3700.0)

# TC-04: top slab applies above 500 (3700 + 50@12 = 4300)
check("slab_charge(550) = 4300", sol.slab_charge(550) == 4300.0)

# TC-05: fixed charge + 2% cess present in every bill
b = sol.compute_bill(100, None)
check("fixed charge 50 included", b["fixed"] == 50.0)
check("cess = 2% of energy (500 -> 10)", b["cess"] == 10.0)

# TC-06: rebate given when consumption falls vs previous month
b_down = sol.compute_bill(310, 390)
check("rebate applied on decrease", b_down["rebate"] > 0)

# TC-07: no rebate on increase
b_up = sol.compute_bill(390, 245)
check("no rebate on increase", b_up["rebate"] == 0.0)

# TC-08: unusual-increase threshold is 30%
change = (390 - 245) / 245
check("Jul->Aug flagged as unusual (>30%)", change > sol.UNUSUAL_INCREASE)

# TC-09: bill total arithmetic (100 units: 500 + 50 + 10 - 0 = 560)
check("total for 100 units = 560", sol.compute_bill(100, None)["total"] == 560.0)

# TC-10: five months of data processed
check("5 months supplied", len(sol.MONTHS) == 5)

print("\nALL %d TESTS PASSED (Case Study 02)" % passed)
