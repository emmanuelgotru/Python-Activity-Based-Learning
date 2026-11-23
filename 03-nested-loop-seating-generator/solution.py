"""
Case Study 26: Nested Loop Examination Seating Generator
--------------------------------------------------------
Syllabus: nested loops, conditional statements, lists, operators,
pattern / grid generation, input validation.
"""

# ---------------- Classroom configuration ----------------
ROWS = 6
COLS = 8
RESERVED = [(2, 3), (2, 4), (5, 7)]        # (row, col) 1-based, invigilator desks
ALT_ROWS = (2, 4, 6)                       # alternate rows keep only even columns
ALT_BLOCKED_COLS = (1, 3, 5, 7)            # odd columns blocked in those rows


def validate_reserved():
    """Check every reserved seat lies inside the classroom grid."""
    problems = []
    for r, c in RESERVED:
        if not (1 <= r <= ROWS and 1 <= c <= COLS):
            problems.append("reserved seat (%d,%d) is outside %dx%d grid" % (r, c, ROWS, COLS))
    return problems


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


def print_seating(seat):
    print("     " + "  ".join("C%d" % c for c in range(1, COLS + 1)))
    print("     " + "-" * (COLS * 3 - 1))
    for r in range(ROWS):
        cells = "  ".join(seat[r][c] for c in range(COLS))
        print("R%-3d | %s" % (r + 1, cells))
    print("\n  Legend: O = open seat   R = reserved   X = blocked (alternate spacing)")


def count_seats(seat):
    o = r = x = 0
    for row in seat:                       # loop over nested list
        for cell in row:
            if cell == "O":
                o += 1
            elif cell == "R":
                r += 1
            else:
                x += 1
    return o, r, x


def main():
    print("=" * 60)
    print("  EXAMINATION SEATING ARRANGEMENT GENERATOR")
    print("=" * 60)

    problems = validate_reserved()
    if problems:
        print("VALIDATION ERRORS:")
        for p in problems:
            print("  - " + p)
        return

    seat = build_seating()
    print_seating(seat)

    o, r, x = count_seats(seat)
    print("\nSUMMARY")
    print("-" * 60)
    print("  Total grid positions : %d  (%d rows x %d cols)" % (ROWS * COLS, ROWS, COLS))
    print("  Open seats (O)       : %d" % o)
    print("  Reserved seats (R)   : %d" % r)
    print("  Blocked seats (X)    : %d" % x)
    print("  Exam capacity        : %d students" % (o + r))
    print("  Rows fully usable    : %d of %d" %
          (sum(1 for row in seat if "X" not in row), ROWS))

    # ---- demonstrate validation with a bad reserved seat ----
    print("\nVALIDATION DEMO (out-of-range reserved seat):")
    bad = (9, 2)
    if 1 <= bad[0] <= ROWS and 1 <= bad[1] <= COLS:
        print("  seat accepted")
    else:
        print("  ERROR: reserved seat (%d,%d) is outside %dx%d grid"
              % (bad[0], bad[1], ROWS, COLS))


if __name__ == "__main__":
    main()
