# Case Study 27 — Advanced Numeric Pattern Generator

Repository: [Python-Activity-Based-Learning](../README.md)

## 1. Problem Statement

Produce a **hollow diamond** or **symmetric numerical pattern** based on
user-specified dimensions, with **validation for invalid dimensions** and
carefully aligned output.

Patterns implemented:

1. **Hollow diamond** of height `n` (must be an odd integer ≥ 3): edge cells
   show a digit that grows to the centre and shrinks back; interior cells are
   blanks.
2. **Symmetric number pyramid** of height `m` (must be ≥ 1):
   `1 / 121 / 12321 / 1234321 …`, right-aligned by padding.

Invalid dimensions (even, < 3, or negative) must be rejected with a clear
message instead of printing garbage.

## 2. Objectives

- Generate patterns with **nested loops** (row loop + column loop).
- Use **operators** for distance-from-centre and padding arithmetic.
- **Validate dimensions** with conditional statements before printing.
- Maintain careful alignment using string concatenation and space padding.
- Demonstrate both filled-edge (hollow) and mirrored (pyramid) construction.

## 3. Assumptions

- Diamond height must be odd so a single centre row exists; minimum 3.
- Pyramid height must be ≥ 1; there is no upper limit.
- Digits used are 1…9 — practical heights are ≤ 9 for single-digit rows.
- Output is printed to the console, one row per line, left-padded with spaces.
- Dimensions are supplied as integers.

## 4. Algorithm

```
1. START
2. READ n
3. IF n < 3 OR n is even → print "INVALID", go to step 12
4. mid ← n // 2
5. FOR i ← 0 TO n−1 DO
     5.1 dist ← |i − mid|
     5.2 digit ← mid − dist + 1
     5.3 row_len ← 2 × (mid − dist) + 1
     5.4 pad ← (n − row_len) // 2
     5.5 line ← ""
     5.6 FOR j ← 0 TO row_len−1 DO
           IF j = 0 OR j = row_len−1 → line ← line + digit
           ELSE                      → line ← line + " "
         END FOR
     5.7 PRINT spaces(pad) + line
6. END FOR
7. --- pyramid ---
8. READ m ; IF m < 1 → print "INVALID", go to step 12
9. FOR i ← 1 TO m DO
     line ← digits 1..i concatenated, then i−1..1
     PRINT spaces(m − i) + line
10. END FOR
11. PRINT "Done"
12. END
```

## 5. Flowchart

```
              ┌─────────┐
              │  START  │
              └────┬────┘
                   ▼
        ┌──────────────────────┐
        │ READ n (diamond size)│
        └──────────┬───────────┘
                   ▼
        ┌──────────────────────┐     YES   ┌──────────────────┐
        │ n < 3 OR n even ?    ├──────────►│ print INVALID    │
        └──────────┬───────────┘           └────────┬─────────┘
               NO  ▼                                │
        ┌──────────────────────┐                    │
        │ mid ← n // 2         │                    │
        └──────────┬───────────┘                    │
                   ▼                                │
      ┌─────────────────────────┐◄──────────┐       │
      │ FOR i ← 0 TO n−1        │           │       │
      └────────────┬────────────┘           │       │
                   ▼                        │       │
      ┌─────────────────────────┐           │       │
      │ dist = |i − mid|        │           │       │
      │ digit = mid − dist + 1  │           │       │
      │ row_len = 2(mid−dist)+1 │           │       │
      │ pad = (n − row_len) // 2│           │       │
      └────────────┬────────────┘           │       │
                   ▼                        │       │
      ┌─────────────────────────┐           │       │
      │ FOR j ← 0 TO row_len−1  │           │       │
      │  edge? digit : " "      │           │       │
      └────────────┬────────────┘           │       │
                   ▼                        │       │
      ┌─────────────────────────┐           │       │
      │ PRINT pad spaces + line │           │       │
      └────────────┬────────────┘           │       │
                   └──────────┬─────────────┘       │
                              ▼                     │
                   ┌──────────────────────┐         │
                   │ READ m (pyramid)     │         │
                   │ m < 1 ? → INVALID ───┼─────────┤
                   └──────────┬───────────┘         │
                          OK  ▼                     │
      ┌─────────────────────────┐                   │
      │ FOR i ← 1 TO m          │                   │
      │  build 1..i..1 line     │                   │
      │  PRINT pad + line       │                   │
      └────────────┬────────────┘                   │
                   └──────────┬─────────────────────┘
                              ▼
                       ┌─────────────┐
                       │    END      │
                       └─────────────┘
```

## 6. Pseudocode

```
BEGIN NUMERIC_PATTERN_GENERATOR

    FUNCTION hollow_diamond(n):
        IF n < 3 OR n MOD 2 = 0 THEN
            PRINT "INVALID: must be odd and >= 3"
            RETURN FALSE
        END IF
        mid ← n // 2
        FOR i ← 0 TO n−1 DO
            dist ← ABS(i − mid)
            digit ← mid − dist + 1
            row_len ← 2 × (mid − dist) + 1
            pad ← (n − row_len) // 2
            line ← ""
            FOR j ← 0 TO row_len−1 DO
                IF j = 0 OR j = row_len−1 THEN
                    line ← line + STRING(digit)
                ELSE
                    line ← line + " "
                END IF
            END FOR
            PRINT SPACES(pad) + line
        END FOR
        RETURN TRUE
    END FUNCTION

    FUNCTION number_pyramid(m):
        IF m < 1 THEN PRINT "INVALID" ; RETURN FALSE
        FOR i ← 1 TO m DO
            line ← ""
            FOR j ← 1 TO i     DO line ← line + STRING(j)
            FOR j ← i−1 DOWNTO 1 DO line ← line + STRING(j)
            PRINT SPACES(m − i) + line
        END FOR
        RETURN TRUE
    END FUNCTION

    CALL hollow_diamond(5) ; CALL hollow_diamond(7)
    CALL hollow_diamond(6)   → rejected
    CALL number_pyramid(4)   ; CALL number_pyramid(-3) → rejected
END
```

## 7. Python Source Code

Complete, runnable source: **[`solution.py`](./solution.py)**

Key logic (hollow diamond row construction):

```python
def hollow_diamond(n):
    if n < 3 or n % 2 == 0:
        print("  INVALID: size %d -> must be an odd integer >= 3." % n)
        return False
    mid = n // 2
    for i in range(n):
        dist = abs(i - mid)
        digit = str(mid - dist + 1)
        row_len = 2 * (mid - dist) + 1
        pad = (n - row_len) // 2
        line = ""
        for j in range(row_len):
            if j == 0 or j == row_len - 1:
                line += digit
            else:
                line += " "
        print(" " * pad + line)
    return True
```

Run: `python3 solution.py`

## 8. Test Cases

Automated suite: [`test_cases.py`](./test_cases.py) — **9/9 passing**.

| ID | Input | Expected | Actual | Status |
|----|-------|----------|--------|--------|
| TC-01 | `hollow_diamond(5)` | accepted | `True` | PASS |
| TC-02 | size 5 | exactly 5 rows printed | 5 rows | PASS |
| TC-03 | size 5 centre row | `3   3` (hollow) | `3   3` | PASS |
| TC-04 | `hollow_diamond(6)` | rejected (even) | `False` + INVALID | PASS |
| TC-05 | `hollow_diamond(1)` | rejected (< 3) | `False` + INVALID | PASS |
| TC-06 | `number_pyramid(4)` | 4 rows, last `1234321` | matched | PASS |
| TC-07 | `number_pyramid(-3)` | rejected | `False` + INVALID | PASS |
| TC-08 | pyramid top row | centred `1` | `   1` | PASS |
| TC-09 | size 7 run | accepted, 7 rows | `True` | PASS |

## 9. Output

![Output screenshot](output_screenshot.png)

Full text output: [`output.txt`](./output.txt)

```text
PATTERN 1: Hollow diamond, size 7
    1
   2 2
  3   3
 4     4
  3   3
   2 2
    1

PATTERN 1: Validation check (even size 6)
  INVALID: size 6 -> must be an odd integer >= 3.

PATTERN 2: Symmetric number pyramid, size 4
   1
  121
 12321
1234321

PATTERN 2: Validation check (size -3)
  INVALID: size -3 -> must be >= 1.
```

## 10. Conclusion

Both patterns are produced entirely with nested loops, absolute-distance
arithmetic, and space padding — no formatting libraries required. The
validation gate runs before any row is printed, so invalid dimensions (even
sizes, sizes below 3, negatives) yield a clear diagnostic instead of a broken
shape. Tests confirm the hollow interior (`3   3` at the centre of a size-5
diamond), exact row counts, and pyramid symmetry, showing that careful loop
bounds and padding formulas are sufficient for precisely aligned pattern
generation.
