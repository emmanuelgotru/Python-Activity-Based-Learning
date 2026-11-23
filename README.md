# Python-Activity-Based-Learning

**Python Activity-Based Learning — 10 Case Studies with Complete Solutions**

Submission for the Python Programming course. Ten case studies were selected from the
activity list and developed into complete solutions using only the assigned syllabus:
*computational thinking, algorithms, flowcharts, pseudocode, variables, data types,
operators, conditional statements, loops, strings, pattern generation, lists, nested
lists, tuples, tuple operations, and unpacking.*

---

## Selected Case Studies

| # | Case Study | Folder | Key syllabus coverage |
|---|------------|--------|----------------------|
| 1 | University Scholarship Allocation | [`01-university-scholarship-allocation`](01-university-scholarship-allocation/) | lists, tuples, unpacking, conditionals, sorting & tie-breaks |
| 2 | Progressive Electricity Billing | [`02-progressive-electricity-billing`](02-progressive-electricity-billing/) | operators, slabs, percentages, loops, conditionals |
| 3 | Nested Loop Examination Seating Generator | [`03-nested-loop-seating-generator`](03-nested-loop-seating-generator/) | nested loops, grid generation, validation |
| 4 | Advanced Numeric Pattern Generator | [`04-numeric-pattern-generator`](04-numeric-pattern-generator/) | pattern generation, nested loops, input validation |
| 5 | Password Policy Validation Engine | [`05-password-policy-validation`](05-password-policy-validation/) | strings, character classes, boolean logic |
| 6 | Text Compression Using Character Runs | [`06-text-compression-rle`](06-text-compression-rle/) | strings, loops, length comparison, RLE |
| 7 | ATM Menu-Driven Banking Simulation | [`07-atm-banking-simulation`](07-atm-banking-simulation/) | menu loops, validation, lists as logs |
| 8 | Student Marks Matrix Analysis | [`08-student-marks-matrix-analysis`](08-student-marks-matrix-analysis/) | nested lists, row/column statistics |
| 9 | Tuple-Based Course Registration Validation | [`09-tuple-course-registration-validation`](09-tuple-course-registration-validation/) | tuples, nested tuples, unpacking, duplicate detection |
| 10 | Comprehensive Smart Campus Management Simulation | [`10-smart-campus-management-simulation`](10-smart-campus-management-simulation/) | integrated menu-driven simulation (all topics) |

## Deliverables (per case study)

Every folder contains all mandatory deliverables:

| Deliverable | File |
|-------------|------|
| Problem statement, objectives, assumptions, algorithm, flowchart, pseudocode, test cases, conclusion | `README.md` |
| Python source code | `solution.py` |
| Automated test cases (112 assertions across the 10 studies) | `test_cases.py` |
| Program output | `output.txt` |
| Output screenshot | `output_screenshot.png` |
| Sample input (menu-driven programs) | `demo_input.txt` (cases 07 & 10) |

## How to run

```bash
# run a solution
python3 01-university-scholarship-allocation/solution.py

# menu-driven programs use a scripted demo input
python3 07-atm-banking-simulation/solution.py < 07-atm-banking-simulation/demo_input.txt
python3 10-smart-campus-management-simulation/solution.py < 10-smart-campus-management-simulation/demo_input.txt

# run the automated test suite for a case study
python3 01-university-scholarship-allocation/test_cases.py

# run every test suite
for d in */; do python3 "$d/test_cases.py" | tail -1; done
```

**Test status: all 112 automated test cases pass (10/10 case studies).**

## Repository structure

```
Python-Activity-Based-Learning/
├── README.md                          ← this file
├── 01-university-scholarship-allocation/
│   ├── README.md                      ← full documentation + flowchart + pseudocode
│   ├── solution.py                    ← Python source code
│   ├── test_cases.py                  ← automated tests
│   ├── output.txt                     ← captured program output
│   └── output_screenshot.png          ← output screenshot
├── 02-…  …  10-…                      ← same structure for the other 9 studies
```

## Notes

- Only syllabus-approved constructs are used (no libraries beyond the Python
  standard built-ins, no regular expressions, no dictionaries-of-record tricks).
- All data is hypothetical/sample data as permitted by the problem statements.
- Prepared for upload to this GitHub repository as required, to be submitted
  after the Dussehra holidays.
