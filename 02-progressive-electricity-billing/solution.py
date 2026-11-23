"""
Case Study 02: Progressive Electricity Billing
----------------------------------------------
Syllabus: variables, data types, operators, conditional statements, loops,
lists, tuples, tuple unpacking, percentage calculations.
"""

# ---------------- Tariff policy ----------------
# (upper_limit_of_slab, rate_per_unit)
SLABS = [(100, 5.0), (300, 7.0), (500, 9.0), (float("inf"), 12.0)]
FIXED_CHARGE = 50.0
CESS_RATE = 0.02                 # 2 % education cess on energy charge
REBATE_RATE = 0.05               # 5 % rebate when consumption falls vs previous month
UNUSUAL_INCREASE = 0.30          # > 30 % jump month-on-month is "unusual"

# (month, units_consumed)
MONTHS = [
    ("Jun", 180),
    ("Jul", 245),
    ("Aug", 390),
    ("Sep", 310),
    ("Oct", 268),
]


def slab_charge(units):
    """Progressive / slab-wise energy charge."""
    remaining = units
    lower = 0
    charge = 0.0
    for limit, rate in SLABS:
        if remaining <= 0:
            break
        in_slab = min(remaining, limit - lower)
        charge += in_slab * rate
        remaining -= in_slab
        lower = limit
    return charge


def compute_bill(units, prev_units):
    """Return a bill breakdown dictionary for one month."""
    energy = slab_charge(units)
    cess = energy * CESS_RATE
    rebate = 0.0
    if prev_units is not None and units < prev_units:
        rebate = energy * REBATE_RATE
    total = energy + FIXED_CHARGE + cess - rebate
    return {
        "units": units,
        "energy": round(energy, 2),
        "fixed": FIXED_CHARGE,
        "cess": round(cess, 2),
        "rebate": round(rebate, 2),
        "total": round(total, 2),
    }


def main():
    bills = []
    prev = None
    for month, units in MONTHS:
        bill = compute_bill(units, prev)
        bills.append((month, bill))
        prev = units

    print("=" * 82)
    print("  PROGRESSIVE ELECTRICITY BILL STATEMENT")
    print("=" * 82)
    print("%-6s %7s %9s %7s %7s %8s %10s" %
          ("Month", "Units", "Energy", "Fixed", "Cess", "Rebate", "Total( Rs)"))
    print("-" * 82)
    for month, b in bills:
        print("%-6s %7d %9.2f %7.2f %7.2f %8.2f %10.2f" %
              (month, b["units"], b["energy"], b["fixed"], b["cess"], b["rebate"], b["total"]))
    print("-" * 82)

    print("\nMONTH-ON-MONTH COMPARISON:")
    print("-" * 82)
    for i in range(1, len(bills)):
        m0, b0 = bills[i - 1]
        m1, b1 = bills[i]
        change = (b1["units"] - b0["units"]) / b0["units"]
        pct = change * 100
        flag = ""
        if change > UNUSUAL_INCREASE:
            flag = "  << UNUSUAL INCREASE (>30%)"
        elif change < 0:
            flag = "  (decrease -> rebate applied)"
        print("  %s -> %s : %+6.1f%%%s" % (m0, m1, pct, flag))

    print("\nHIGHEST BILL : %s (Rs %.2f)" %
          max(((m, b["total"]) for m, b in bills), key=lambda x: x[1]))
    print("LOWEST  BILL : %s (Rs %.2f)" %
          min(((m, b["total"]) for m, b in bills), key=lambda x: x[1]))


if __name__ == "__main__":
    main()
