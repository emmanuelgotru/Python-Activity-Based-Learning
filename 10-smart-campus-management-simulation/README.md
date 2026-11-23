# Case Study 100 — Comprehensive Smart Campus Management Simulation

Repository: [Python-Activity-Based-Learning](../README.md)

## 1. Problem Statement

Develop a **menu-driven program** that integrates **student records,
attendance, marks, event registration, resource allocation, and summary
reporting** using conditional statements, loops, strings, lists, nested lists,
tuples, and tuple unpacking.

Menu:

```
1. Add student        2. Record attendance
3. Record marks       4. Event registration
5. Transport alloc.   6. Summary report
0. Exit
```

Features:

- **Add student** `(roll, name, dept)` — rejects empty fields and duplicate rolls.
- **Attendance** `(roll, present, total)` — computes % and 75 % eligibility.
- **Marks** — 4 subject marks (0–100 each), average and FIRST/SECOND/THIRD/FAIL.
- **Events** — `TechFest ₹200`, `CulturalNight ₹150`, `SportsMeet ₹100`;
  rejects unknown rolls and duplicate registrations; tracks revenue.
- **Transport** — per route: demand, bus capacity, buses available →
  served / unserved passengers; fleet limited to 6 buses.
- **Summary** — prints every record and aggregate totals.

## 2. Objectives

- Integrate all syllabus topics in one **menu-driven `while` loop**.
- Store records as **tuples inside lists**; **unpack** them for reporting.
- Validate every input with conditionals before mutating state.
- Compute aggregates (revenue, unserved passengers) with loops.
- Produce a consolidated summary report.

## 3. Assumptions

- Single-session in-memory data (no file storage) — starts empty each run.
- Attendance eligibility threshold 75 %; grades: FIRST ≥ 75, SECOND ≥ 60,
  THIRD ≥ 40, else FAIL.
- Marks are integers 0–100; exactly 4 subjects.
- Transport: served = min(demand, buses × capacity); unserved = remainder.
- Maximum 6 buses in the fleet.
- Demo input scripted in `demo_input.txt` for reproducible output.

## 4. Algorithm

```
1. START
2. students ← [] ; attendance ← [] ; marks_records ← []
   event_regs ← [] ; route_stats ← []
3. LOOP:
   3.1 PRINT menu ; READ choice
   3.2 CASE choice:
     "1": READ roll, name, dept
          IF empty or duplicate roll → REJECT
          ELSE students.append((roll, name, dept))
     "2": READ roll, present, total
          IF unknown roll or invalid numbers → REJECT
          ELSE append (roll, present, total);
               pct = present/total×100 ; flag ≥ 75 %
     "3": READ roll, 4 marks
          IF unknown roll, ≠4 marks, or out of 0–100 → REJECT
          ELSE append (roll, marks); avg; grade FIRST/SECOND/THIRD/FAIL
     "4": READ roll, event choice
          IF unknown roll / bad choice / already registered → REJECT
          ELSE append (roll, event_name, fee)
     "5": READ route, demand, capacity, buses
          IF invalid values or buses > 6 → REJECT
          ELSE served = min(demand, buses×capacity);
               append (route, demand, capacity, buses)
     "6": FOR each student tuple: unpack & PRINT
          revenue = Σ fees ; unserved = Σ (demand − served)
          PRINT all aggregates
     "0": PRINT goodbye ; BREAK
     DEFAULT: REJECT unknown option
4. END LOOP
5. END
```

## 5. Flowchart

```
                 ┌─────────┐
                 │  START  │
                 └────┬────┘
                      ▼
        ┌──────────────────────────┐
        │ init empty record lists  │
        └─────────────┬────────────┘
                      ▼
     ┌───────────────────────────────┐◄──────────────┐
     │ PRINT menu ; READ choice      │               │
     └───────────────┬───────────────┘               │
                     ▼                               │
   ┌──────────────────────────────────┐              │
   │ 1? validate roll/name/dept       │              │
   │    → students += (roll,name,dept)│              │
   │ 2? validate attendance numbers   │              │
   │    → attendance += tuple, flag % │              │
   │ 3? validate 4 marks in 0–100     │              │
   │    → marks_records += tuple      │              │
   │ 4? validate event choice         │              │
   │    → event_regs += tuple, revenue│              │
   │ 5? validate route numbers, ≤6 bus│              │
   │    → route_stats += tuple        │              │
   └──────────────────┬───────────────┘              │
                      ▼                              │
   ┌──────────────────────────────────┐              │
   │ 6? summary:                      │              │
   │   FOR each tuple → unpack & print│              │
   │   Σ revenue, Σ unserved          │              │
   │ 0? goodbye → BREAK ──────────────┼──────────────┤
   │ other? REJECT ───────────────────┼──────────────┘
   └──────────────────────────────────┘
                      ▼
               ┌─────────────┐
               │    END      │
               └─────────────┘
```

## 6. Pseudocode

```
BEGIN SMART_CAMPUS_SIMULATION

    students ← [] ; attendance ← [] ; marks_records ← []
    event_regs ← [] ; route_stats ← []
    EVENTS ← [("TechFest",200), ("CulturalNight",150), ("SportsMeet",100)]
    TOTAL_BUSES ← 6

    REPEAT
        PRINT menu
        READ choice
        CASE choice OF
            "1": READ roll, name, dept
                 IF roll = "" OR name = "" OR roll EXISTS THEN REJECT
                 ELSE APPEND (roll, name, dept) TO students

            "2": READ roll, present, total
                 IF roll UNKNOWN OR total ≤ 0 OR present ∉ [0..total] THEN REJECT
                 ELSE APPEND (roll, present, total) TO attendance
                      pct ← present × 100 / total
                      PRINT eligibility (≥ 75 %)

            "3": READ roll, marks(4)
                 IF roll UNKNOWN OR count ≠ 4 OR any mark ∉ [0..100] THEN REJECT
                 ELSE APPEND (roll, marks) TO marks_records
                      avg ← Σ marks / 4
                      grade ← FIRST / SECOND / THIRD / FAIL

            "4": READ roll, choice
                 IF roll UNKNOWN OR choice invalid OR already registered THEN REJECT
                 ELSE (name, fee) ← EVENTS[choice−1]
                      APPEND (roll, name, fee) TO event_regs

            "5": READ route, demand, capacity, buses
                 IF invalid OR buses > TOTAL_BUSES THEN REJECT
                 ELSE served ← MIN(demand, buses × capacity)
                      APPEND (route, demand, capacity, buses) TO route_stats

            "6": FOR (roll,name,dept) IN students DO PRINT END FOR
                 revenue ← Σ fee  (FOR (roll,ev,fee) IN event_regs)
                 unserved ← Σ (demand − MIN(demand, buses×capacity))
                 PRINT totals

            "0": PRINT "Session ended" ; EXIT
            DEFAULT: REJECT
        END CASE
    UNTIL choice = "0"
END
```

## 7. Python Source Code

Complete, runnable source: **[`solution.py`](./solution.py)**

Key logic (attendance + transport allocation):

```python
def record_attendance():
    roll = input("  Roll no: ").strip().upper()
    if find_student(roll) is None:
        print("  REJECTED: unknown roll %s." % roll)
        return
    try:
        present = int(input("  Classes attended: ").strip())
        total = int(input("  Classes held     : ").strip())
    except ValueError:
        print("  REJECTED: numbers only.")
        return
    if total <= 0 or present < 0 or present > total:
        print("  REJECTED: invalid attendance values.")
        return
    attendance.append((roll, present, total))
    pct = present * 100.0 / total
    verdict = "ELIGIBLE" if pct >= 75 else "NOT ELIGIBLE (<75%)"
    print("  %s attendance = %.1f%% -> %s" % (roll, pct, verdict))
```

Run (interactive): `python3 solution.py`
Run (scripted demo): `python3 solution.py < demo_input.txt`

## 8. Test Cases

Automated suite: [`test_cases.py`](./test_cases.py) — **16/16 passing**.

| ID | Input | Expected | Actual | Status |
|----|-------|----------|--------|--------|
| TC-01 | add A1 Ananya CSE | stored as tuple | `("A1","Ananya","CSE")` | PASS |
| TC-02 | add A1 again | duplicate rejected | still 1 student | PASS |
| TC-03 | add with empty roll | rejected | still 1 student | PASS |
| TC-04 | attendance A1 18/20 | 90 % ELIGIBLE, tuple stored | `("A1",18,20)` | PASS |
| TC-05 | attendance A1 13/20 | 65 % NOT ELIGIBLE | flagged | PASS |
| TC-06 | attendance 25/20 | present > total rejected | unchanged | PASS |
| TC-07a | marks 85 78 90 82 | avg 83.75 recorded | avg=83.75 | PASS |
| TC-07b | same marks | grade FIRST (avg ≥ 75) | FIRST | PASS |
| TC-08 | mark 101 | out-of-range rejected | 1 record kept | PASS |
| TC-09 | event choice 1 | TechFest registered, fee 200 | fee 200 | PASS |
| TC-10 | same event again | duplicate rejected | 1 registration | PASS |
| TC-11 | route R1 180/40×4 | served 160, unserved 20 | `unserved=20` | PASS |
| TC-12a | summary | reports 1 student | "Students on roll : 1" | PASS |
| TC-12b | summary | revenue ₹200 | "revenue Rs 200" | PASS |
| TC-13a | `find_student("A1")` | returns Ananya | Ananya | PASS |
| TC-13b | `find_student("Z9")` | returns None | None | PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full text output: [`output.txt`](./output.txt) · scripted input: [`demo_input.txt`](./demo_input.txt)

```text
  CAMPUS SUMMARY REPORT
  Students on roll : 2
     A1     Ananya       CSE
     A2     Bharat       ECE
  Attendance records: 1
     A2     13/20 = 65.0%
  Marks records: 2
     A1     [85, 78, 90, 82] avg=83.75
     A2     [55, 48, 62, 70] avg=58.75
  Event registrations: 2  ->  revenue Rs 350
     route R1     demand=180 served=160 unserved=20
     route R2     demand=60 served=60 unserved=0
  Total unserved passengers: 20
```

The scripted demo also exercises rejections: duplicate roll `A1`, attendance
25/20 (impossible), a mark of 101, and a duplicate event registration — each
refused with a message while existing records stay intact.

## 10. Conclusion

This integrated simulation ties together every syllabus topic in one coherent
program: a `while` menu loop dispatches to six features; records live as
tuples inside lists and are unpacked for reporting; strings are normalised for
roll numbers; conditionals and try/except guard every input; and loops compute
revenue (₹350) and unserved passengers (20) for the summary. The 16 automated
tests verify both the happy paths and each rejection path, proving that a
well-structured menu-driven design can safely combine student records,
attendance, marks, events and resource allocation in a single maintainable
program.
