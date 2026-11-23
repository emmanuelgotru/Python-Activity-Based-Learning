# Case Study 02 — Progressive Electricity Billing

Repository: [Python-Activity-Based-Learning](../README.md)

## 1. Problem Statement

Calculate household electricity bills using **multiple consumption slabs**, fixed
charges, surcharges, and rebates, then **compare bills across several months**
and **identify unusual increases**.

Tariff policy used:

| Slab | Units | Rate (₹/unit) |
|------|-------|---------------|
| 1 | 0 – 100 | 5 |
| 2 | 101 – 300 | 7 |
| 3 | 301 – 500 | 9 |
| 4 | above 500 | 12 |

- Fixed charge: ₹50 per month
- Surcharge: 2 % education cess on the energy charge
- Rebate: 5 % of energy charge when this month's consumption is lower than the
  previous month's
- Unusual increase: any month-on-month jump greater than 30 %

## 2. Objectives

- Implement **progressive (slab) tariff** arithmetic with operators and loops.
- Apply **conditional statements** for cess, rebate, and flagging rules.
- Store multi-month data in a **list of tuples** and **unpack** it while iterating.
- Compute percentage changes and compare across months.
- Produce a formatted statement plus a comparison report.

## 3. Assumptions

- Slabs are applied progressively (only the units falling in each slab are
  charged at that slab's rate).
- Cess is computed on the energy charge only (not on fixed charge).
- Rebate applies only when consumption decreases vs. the immediately previous
  month; the first month has no previous month, hence no rebate.
- A rise > 30 % (strictly) is "unusual"; equal-to-30 % is not flagged.
- All amounts are in ₹; data is hypothetical.

## 4. Algorithm

```
1. START
2. Define SLABS, FIXED=50, CESS=2%, REBATE=5%, UNUSUAL=30%
3. READ list of (month, units)
4. prev ← None
5. FOR each (month, units) DO
   5.1 energy ← 0; remaining ← units; lower ← 0
   5.2 FOR each (limit, rate) in SLABS DO
         in_slab ← min(remaining, limit − lower)
         energy ← energy + in_slab × rate
         remaining ← remaining − in_slab; lower ← limit
         IF remaining ≤ 0 → exit inner loop
       END FOR
   5.3 cess     ← energy × 0.02
   5.4 rebate  ← (prev ≠ None AND units < prev) ? energy × 0.05 : 0
   5.5 total   ← energy + 50 + cess − rebate
   5.6 STORE bill;  prev ← units
6. END FOR
7. PRINT bill table for all months
8. FOR each consecutive pair of months DO
     change ← (u2 − u1) / u1
     IF change > 0.30 → flag "UNUSUAL INCREASE"
     ELSE IF change < 0 → note "rebate applied"
9. PRINT highest / lowest bill
10. END
```

## 5. Flowchart

```
                 ┌─────────┐
                 │  START  │
                 └────┬────┘
                      ▼
        ┌───────────────────────────┐
        │ load tariff slabs, fixed, │
        │ cess, rebate, month data  │
        └─────────────┬─────────────┘
                      ▼
             ┌────────────────┐
             │ prev ← None    │
             └───────┬────────┘
                     ▼
       ┌──────────────────────────┐◄─────────────┐
       │ FOR (month, units) in data│             │
       └────────────┬─────────────┘             │
                    ▼                           │
       ┌──────────────────────────┐             │
       │ loop through slabs:      │             │
       │ energy += in_slab × rate │             │
       └────────────┬─────────────┘             │
                    ▼                           │
       ┌──────────────────────────┐             │
       │ cess = energy × 0.02     │             │
       │ rebate = (units<prev)    │             │
       │   ? energy × 0.05 : 0    │             │
       │ total = energy+50+cess   │             │
       │          − rebate        │             │
       │ store bill, prev = units │             │
       └────────────┬─────────────┘             │
                    └─────────────┬─────────────┘
                                  ▼
                    ┌──────────────────────────┐
                    │ print statement table    │
                    └────────────┬─────────────┘
                                 ▼
                  ┌────────────────────────────┐◄──────┐
                  │ FOR consecutive month pairs│       │
                  └────────────┬───────────────┘       │
                               ▼                       │
                 ┌──────────────────────────┐          │
                 │ change = Δunits / units  │          │
                 │ change>30% ? FLAG unusual│          │
                 │ change<0   ? note rebate │          │
                 └────────────┬─────────────┘          │
                              └──────────┬─────────────┘
                                         ▼
                              ┌──────────────────────┐
                              │ print max/min bills  │
                              └──────────┬───────────┘
                                         ▼
                                  ┌─────────────┐
                                  │    END      │
                                  └─────────────┘
```

## 6. Pseudocode

```
BEGIN ELECTRICITY_BILLING

    SLABS ← [(100,5), (300,7), (500,9), (∞,12)]
    FIXED ← 50 ; CESS ← 0.02 ; REBATE ← 0.05 ; UNUSUAL ← 0.30

    FUNCTION slab_charge(units):
        remaining ← units ; lower ← 0 ; charge ← 0
        FOR (limit, rate) IN SLABS DO
            IF remaining ≤ 0 THEN BREAK
            in_slab ← MIN(remaining, limit − lower)
            charge ← charge + in_slab × rate
            remaining ← remaining − in_slab
            lower ← limit
        END FOR
        RETURN charge
    END FUNCTION

    prev ← NONE
    FOR (month, units) IN MONTHS DO
        energy ← slab_charge(units)
        cess   ← energy × CESS
        rebate ← (prev ≠ NONE AND units < prev) × energy × REBATE
        total  ← energy + FIXED + cess − rebate
        APPEND (month, total) TO bills
        prev ← units
    END FOR

    FOR i ← 1 TO LENGTH(bills) DO
        change ← (units[i] − units[i−1]) / units[i−1]
        IF change > UNUSUAL THEN PRINT "UNUSUAL INCREASE"
        ELSE IF change < 0   THEN PRINT "rebate applied"
    END FOR

    PRINT maximum and minimum bill
END
```

## 7. Python Source Code

Complete, runnable source: **[`solution.py`](./solution.py)**

Key logic (slab charge + bill with rebate):

```python
def slab_charge(units):
    remaining, lower, charge = units, 0, 0.0
    for limit, rate in SLABS:
        if remaining <= 0:
            break
        in_slab = min(remaining, limit - lower)
        charge += in_slab * rate
        remaining -= in_slab
        lower = limit
    return charge

def compute_bill(units, prev_units):
    energy = slab_charge(units)
    cess = energy * CESS_RATE
    rebate = energy * REBATE_RATE if (prev_units is not None and units < prev_units) else 0.0
    total = energy + FIXED_CHARGE + cess - rebate
    return {"energy": energy, "cess": cess, "rebate": rebate, "total": round(total, 2)}
```

Run: `python3 solution.py`

## 8. Test Cases

Automated suite: [`test_cases.py`](./test_cases.py) — **11/11 passing**.

| ID | Input | Expected | Actual | Status |
|----|-------|----------|--------|--------|
| TC-01 | 100 units | ₹500 energy (all slab 1) | 500.0 | PASS |
| TC-02 | 300 units | ₹1900 (100×5 + 200×7) | 1900.0 | PASS |
| TC-03 | 500 units | ₹3700 (1900 + 200×9) | 3700.0 | PASS |
| TC-04 | 550 units | ₹4300 (3700 + 50×12) | 4300.0 | PASS |
| TC-05 | any bill | fixed ₹50 included | fixed = 50.0 | PASS |
| TC-06 | 100 units | cess = 2% of 500 = ₹10 | 10.0 | PASS |
| TC-07 | 310 after 390 (↓) | rebate > 0 | rebate 99.50 | PASS |
| TC-08 | 390 after 245 (↑) | no rebate | 0.0 | PASS |
| TC-09 | Jul→Aug +59.2 % | flagged unusual (>30 %) | flagged | PASS |
| TC-10 | 100 units bill | total = 500+50+10 = 560 | 560.0 | PASS |
| TC-11 | month list | 5 months supplied | 5 | PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full text output: [`output.txt`](./output.txt)

```text
Month    Units    Energy   Fixed    Cess   Rebate Total( Rs)
Jun        180   1060.00   50.00   21.20     0.00    1131.20
Jul        245   1515.00   50.00   30.30     0.00    1595.30
Aug        390   2710.00   50.00   54.20     0.00    2814.20
Sep        310   1990.00   50.00   39.80    99.50    1980.30
Oct        268   1676.00   50.00   33.52    83.80    1675.72

  Jun -> Jul :  +36.1%  << UNUSUAL INCREASE (>30%)
  Jul -> Aug :  +59.2%  << UNUSUAL INCREASE (>30%)
  Aug -> Sep :  -20.5%  (decrease -> rebate applied)
  Sep -> Oct :  -13.5%  (decrease -> rebate applied)

HIGHEST BILL : Aug (Rs 2814.20)
```

## 10. Conclusion

The billing engine correctly applies four progressive slabs, the fixed charge,
2 % cess, and the conservation rebate, producing statements that match manual
computation for every test case. Month-on-month comparison successfully
identified the two unusual jumps (Jun→Jul +36.1 %, Jul→Aug +59.2 %) and
acknowledged rebate-eligible decreases. The design separates tariff policy
(constants) from computation (functions), so a change in slab rates requires
editing only the `SLABS` table — demonstrating clean algorithmic decomposition
using only loops, conditionals, and operators.
