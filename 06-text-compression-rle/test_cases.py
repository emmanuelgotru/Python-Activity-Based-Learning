"""Automated test cases for Case Study 35 - Text Compression Using Character Runs."""
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


# TC-01: simple run encoding
check("encode('aaabbbccc') = a3b3c3", sol.encode("aaabbbccc") == "a3b3c3")

# TC-02: single characters encoded with count 1
check("encode('python') = p1y1t1h1o1n1", sol.encode("python") == "p1y1t1h1o1n1")

# TC-03: long single run compresses to 3 chars
check("encode of 20 a's = 'a20'", sol.encode("a" * 20) == "a20")

# TC-04: empty string stays empty
check("encode('') = ''", sol.encode("") == "")

# TC-05: alternating characters never merge
check("'ababab' -> a1b1a1b1a1b1", sol.encode("ababab") == "a1b1a1b1a1b1")

# TC-06: compression beneficial for repetitive text
s = "aaaaaaaaaaaaaaaaaaaa"
check("beneficial: 20 a's shrink", len(sol.encode(s)) < len(s))

# TC-07: compression NOT beneficial for random text
s = "python"
check("not beneficial: 'python' grows", len(sol.encode(s)) > len(s))

# TC-08: boundary - equal length counts as not beneficial
s = "aabb"
check("boundary: 'aabb' length equal", len(sol.encode(s)) == len(s))

# TC-09: mixed runs in 'mississippi'
check("encode('mississippi') correct", sol.encode("mississippi") == "m1i1s2i1s2i1p2i1")

# TC-10: encoded length arithmetic (13 -> 8 for aaabbbcccdddd)
s = "aaabbbcccdddd"
check("aaabbbcccdddd: 13 -> 8", len(sol.encode(s)) == 8)

print("\nALL %d TESTS PASSED (Case Study 35)" % passed)
