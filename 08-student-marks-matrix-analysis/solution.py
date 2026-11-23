"""
Case Study 42: Student Marks Matrix Analysis
--------------------------------------------
Syllabus: nested lists, conditional statements, loops, operators,
row-wise / column-wise statistics, max/min with position.
"""

SUBJECTS = ["Maths", "Physics", "Chemistry", "English", "CS"]
STUDENTS = ["Ananya", "Bharat", "Chitra", "Deepak", "Fatima"]

# rows = students, columns = subjects
MARKS = [
    [82, 76, 90, 71, 85],
    [55, 48, 62, 70, 58],
    [74, 69, 71, 66, 80],
    [61, 57, 64, 59, 66],
    [91, 88, 94, 87, 96],
]

WEAK_SUBJECT_AVERAGE = 70.0
AT_RISK_AVERAGE = 60.0


def grade_of(avg):
    if avg >= 85:
        return "A (Distinction)"
    if avg >= 70:
        return "B (First Class)"
    if avg >= 55:
        return "C (Second Class)"
    return "D (Third Class)"


def main():
    # ---------- display the matrix ----------
    print("=" * 74)
    print("  STUDENT MARKS MATRIX ANALYSIS")
    print("=" * 74)
    header = "%-9s" % "Student" + "".join("%10s" % s for s in SUBJECTS) + "%9s" % "Avg"
    print(header)
    print("-" * 74)
    for r in range(len(STUDENTS)):
        row = MARKS[r]
        avg = sum(row) / len(row)
        print("%-9s" % STUDENTS[r] + "".join("%10d" % m for m in row) + "%9.2f" % avg)
    print("-" * 74)

    # ---------- row-wise statistics ----------
    print("\nROW-WISE (per student):")
    best_total = -1
    best_index = -1
    for r in range(len(STUDENTS)):
        total = sum(MARKS[r])
        avg = total / len(MARKS[r])
        status = "AT RISK" if avg < AT_RISK_AVERAGE else "ok"
        print("  %-9s total=%3d  avg=%5.2f  grade=%-18s %s"
              % (STUDENTS[r], total, avg, grade_of(avg), status))
        if total > best_total:
            best_total = total
            best_index = r
    print("  -> Top performer: %s (%d marks)" % (STUDENTS[best_index], best_total))

    # ---------- column-wise statistics ----------
    print("\nCOLUMN-WISE (per subject):")
    weak = []
    for c in range(len(SUBJECTS)):
        total = 0
        for r in range(len(STUDENTS)):
            total += MARKS[r][c]
        avg = total / len(STUDENTS)
        flag = ""
        if avg < WEAK_SUBJECT_AVERAGE:
            flag = "  << WEAK SUBJECT"
            weak.append(SUBJECTS[c])
        print("  %-10s average = %5.2f%s" % (SUBJECTS[c], avg, flag))

    # ---------- extremes ----------
    high = -1
    low = 101
    hi_pos = lo_pos = (0, 0)
    for r in range(len(STUDENTS)):
        for c in range(len(SUBJECTS)):
            if MARKS[r][c] > high:
                high = MARKS[r][c]
                hi_pos = (r, c)
            if MARKS[r][c] < low:
                low = MARKS[r][c]
                lo_pos = (r, c)
    print("\nEXTRAMES:")
    print("  Highest: %d (%s in %s)" % (high, STUDENTS[hi_pos[0]], SUBJECTS[hi_pos[1]]))
    print("  Lowest : %d (%s in %s)" % (low, STUDENTS[lo_pos[0]], SUBJECTS[lo_pos[1]]))
    print("  Weak subjects (avg < %.0f): %s" %
          (WEAK_SUBJECT_AVERAGE, ", ".join(weak) if weak else "none"))


if __name__ == "__main__":
    main()
