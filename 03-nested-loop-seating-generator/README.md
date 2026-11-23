# Case Study 26 — Nested Loop Examination Seating Generator

Repository: [Python-Activity-Based-Learning](../README.md)

## 1. Problem Statement

Generate a **seating arrangement** for an examination hall with row and column
identifiers, **reserved positions**, **alternate seating restrictions**, and a
fixed classroom capacity — using **nested loops**.

Configuration used:

- Classroom grid: **6 rows × 8 columns** (48 positions)
- Reserved seats (invigilator desks): `(2,3), (2,4), (5,7)` — 1-based
- Alternate-spacing rule: in even rows (2, 4, 6), only **even columns** may be
  seated; odd columns in those rows are blocked
- The system must validate reserved seats lie inside the grid, print the full
  labelled grid, and summarise open / reserved / blocked counts.

## 2. Objectives

- Build a 2-D grid with **nested loops** (rows outer, columns inner).
- Apply **conditional statements** for reserved and alternate-spacing rules.
- Validate input data (reserved seats inside bounds).
- Count and report seat categories by iterating a **nested list**.
- Print an aligned, labelled seating chart.

## 3. Assumptions

- Rows and columns are numbered from 1 in the display, 0-based in the list.
- Reserved seats take priority over the alternate-spacing block.
- "Exam capacity" = open + reserved seats (blocked seats cannot be used).
- The alternate rule applies only to even rows' odd columns; all other cells
  are open unless reserved.
- Data is hypothetical.

## 4. Algorithm

```
1. START
2. SET ROWS=6, COLS=8, RESERVED=[(2,3),(2,4),(5,7)],
   ALT_ROWS=[2,4,6], ALT_BLOCKED=[1,3,5,7]
3. FOR each (r,c) in RESERVED DO
     IF r<1 OR r>ROWS OR c<1 OR c>COLS → print error, STOP
4. END FOR
5. SET seat ← empty nested list
6. FOR r ← 1 TO ROWS DO
     row ← []
     FOR c ← 1 TO COLS DO
        IF (r,c) ∈ RESERVED          → row.append("R")
        ELSE IF r ∈ ALT_ROWS AND c ∈ ALT_BLOCKED
                                      → row.append("X")
        ELSE                          → row.append("O")
     END FOR
     append row TO seat
7. END FOR
8. PRINT column headers C1..C8, then FOR each row print "Rn | cells"
9. COUNT O, R, X by nested iteration; capacity ← O + R
10. PRINT summary; also demo validation with an out-of-range seat
11. END
```

## 5. Flowchart

```
                ┌─────────┐
                │  START  │
                └────┬────┘
                     ▼
       ┌──────────────────────────┐
       │ set ROWS, COLS, RESERVED,│
       │ alternate-row rules      │
       └────────────┬─────────────┘
                    ▼
        ┌───────────────────────┐
        │ FOR each reserved seat│
        │ inside grid?          │──NO──► print ERROR → END
        └───────────┬───────────┘
                 YES│
                    ▼
     ┌──────────────────────────────┐
     │ seat ← []                    │
     └──────────────┬───────────────┘
                    ▼
      ┌─────────────────────────┐◄───────────────┐
      │ FOR r ← 1 TO ROWS       │                │
      └────────────┬────────────┘                │
                   ▼                             │
        ┌───────────────────────┐                │
        │ FOR c ← 1 TO COLS     │                │
        └──────────┬────────────┘                │
                   ▼                             │
        ┌──────────────────────────┐             │
        │ (r,c) reserved?  → "R"   │             │
        │ elif alt-row & odd col   │             │
        │            → "X"         │             │
        │ else        → "O"        │             │
        └────────────┬─────────────┘             │
                     └──────────┬────────────────┘
                                ▼
                  ┌─────────────────────────┐
                  │ PRINT labelled grid     │
                  │ COUNT O / R / X         │
                  │ capacity = O + R        │
                  └────────────┬────────────┘
                               ▼
                        ┌─────────────┐
                        │    END      │
                        └─────────────┘
```

## 6. Pseudocode

```
BEGIN SEATING_GENERATOR

    ROWS ← 6 ; COLS ← 8
    RESERVED ← [(2,3), (2,4), (5,7)]
    ALT_ROWS ← [2,4,6] ; ALT_BLOCKED ← [1,3,5,7]

    FOR (r,c) IN RESERVED DO
        IF r ∉ [1..ROWS] OR c ∉ [1..COLS] THEN
            PRINT "reserved seat outside grid" ; STOP
    END FOR

    seat ← []
    FOR r ← 1 TO ROWS DO
        row ← []
        FOR c ← 1 TO COLS DO
            IF (r,c) IN RESERVED THEN              row ← row + "R"
            ELSE IF r IN ALT_ROWS AND c IN ALT_BLOCKED THEN
                row ← row + "X"
            ELSE
                row ← row + "O"
            END IF
        END FOR
        APPEND row TO seat
    END FOR

    PRINT headers
    FOR r ← 1 TO ROWS DO
        PRINT "R" + r + " |" + JOIN(seat[r−1], "  ")
    END FOR

    o ← 0 ; rcount ← 0 ; x ← 0
    FOR each row IN seat DO
        FOR each cell IN row DO
            IF cell = "O" THEN o ← o+1
            ELSE IF cell = "R" THEN rcount ← rcount+1
            ELSE x ← x+1
        END FOR
    END FOR

    PRINT "capacity = " + o + rcount
END
```

## 7. Python Source Code

Complete, runnable source: **[`solution.py`](./solution.py)**

Key logic (grid construction with nested loops):

```python
def build_seating():
    """Nested list: 'O' open, 'R' reserved, 'X' blocked by alternate rule."""
    seat = []
    for r in range(1, ROWS + 1):
        row = []
        for c in range(1, COLS + 1):
            if (r, c) in RESERVED:
                row.append("R")
            elif r in ALT_ROWS and c in ALT_BLOCKED_COLS:
                row.append("X")
            else:
                row.append("O")
        seat.append(row)
    return seat
```

Run: `python3 solution.py`

## 8. Test Cases

Automated suite: [`test_cases.py`](./test_cases.py) — **12/12 passing**.

| ID | Input | Expected | Actual | Status |
|----|-------|----------|--------|--------|
| TC-01 | build grid | 6 rows | 6 | PASS |
| TC-02 | each row | 8 columns | 8 for all rows | PASS |
| TC-03 | reserved (2,3) | cell = "R" | "R" | PASS |
| TC-04 | reserved (5,7) | cell = "R" | "R" | PASS |
| TC-05 | (2,1) odd col in alt row | "X" blocked; (1,1) stays "O" | X / O | PASS |
| TC-06 | (4,5) | "X" blocked | "X" | PASS |
| TC-07 | (2,2) even col alt row | open "O" | "O" | PASS |
| TC-08 | reserved vs alt rule | reserved wins ("R") | "R" | PASS |
| TC-09 | default RESERVED list | valid (no errors) | `[]` | PASS |
| TC-10 | reserved (9,2) | out-of-range flagged | 1 problem, "outside" | PASS |
| TC-11 | seat counts | O+R+X = 48 | 34+3+11 = 48 | PASS |
| TC-12 | reserved count | 3 | 3 | PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full text output: [`output.txt`](./output.txt)

```text
     C1  C2  C3  C4  C5  C6  C7  C8
     ---------------------------------
R1   | O   O   O   O   O   O   O   O
R2   | X   O   R   R   O   O   O   O
R3   | O   O   O   O   O   O   O   O
R4   | X   O   X   O   X   O   X   O
R5   | O   O   O   O   O   O   O   R
R6   | X   O   X   O   X   O   X   O

SUMMARY
  Total grid positions : 48  (6 rows x 8 cols)
  Open seats (O)       : 34
  Reserved seats (R)   : 3
  Blocked seats (X)    : 11
  Exam capacity        : 37 students
```

## 10. Conclusion

The generator builds a fully labelled 6×8 seating chart with two interacting
rules (reserved desks and alternate-spacing) purely through nested loops and
conditional checks. Validation correctly rejects an out-of-range reserved seat
before any output is produced, and the summary accounts for all 48 grid
positions (34 open + 3 reserved + 11 blocked = 48). The same nested-list
approach scales to any classroom size by changing three constants, and the
automated tests pin down every rule including the reserved-over-blocked
priority.
