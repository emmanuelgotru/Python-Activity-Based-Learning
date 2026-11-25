# Case Study 38 — ATM Menu-Driven Banking Simulation

## Problem statement

Implement repeated menu operations for deposits, withdrawals, balance inquiries and transaction summaries, with validation and account limits.

## Objectives

Drive the program with a menu loop; validate every amount before changing state; keep a list of transaction tuples and unpack it for the mini statement; handle non-numeric input without crashing.

## Assumptions

Opening balance Rs 5,000. Deposits must be positive and at most Rs 1,00,000. Withdrawals must be positive multiples of Rs 100, at most Rs 10,000, and must leave at least Rs 1,000 in the account. Single account, no interest. Sample input is scripted in demo_input.txt.

## Algorithm

```
1. START
2. balance ← 5000 ; log ← []
3. LOOP:
   3.1 PRINT menu (1 Deposit, 2 Withdraw, 3 Balance, 4 Statement, 5 Exit)
   3.2 READ choice
   3.3 IF choice = 1:
         READ amount ; if non-numeric → reject
         IF amount ≤ 0 or > 100000 → reject
         ELSE balance += amount ; log.append(("DEPOSIT", amount, balance))
   3.4 IF choice = 2:
         READ amount ; if non-numeric → reject
         IF amount ≤ 0                → reject
         ELSE IF amount % 100 ≠ 0     → reject
         ELSE IF amount > 10000       → reject
         ELSE IF balance − amount < 1000 → reject
         ELSE balance −= amount ; log.append(("WITHDRAW", amount, balance))
   3.5 IF choice = 3 → PRINT balance
   3.6 IF choice = 4 → FOR each (kind, amt, bal) in log: PRINT row
   3.7 IF choice = 5 → PRINT session summary ; BREAK
   3.8 ELSE → PRINT "unknown option"
4. END LOOP
5. END
```

## Flowchart

![Flowchart](flowchart.png)

## Pseudocode

```
BEGIN ATM_SIMULATION

    balance ← 5000 ; log ← []
    MIN_BALANCE ← 1000 ; MAX_WITHDRAW ← 10000 ; MAX_DEPOSIT ← 100000

    FUNCTION deposit(amount):
        IF amount ≤ 0 OR amount > MAX_DEPOSIT THEN RETURN "REJECTED"
        balance ← balance + amount
        APPEND ("DEPOSIT", amount, balance) TO log
        RETURN "accepted"
    END FUNCTION

    FUNCTION withdraw(amount):
        IF amount ≤ 0                    THEN RETURN "REJECTED"
        IF amount MOD 100 ≠ 0            THEN RETURN "REJECTED: multiple of 100"
        IF amount > MAX_WITHDRAW         THEN RETURN "REJECTED: limit"
        IF balance − amount < MIN_BALANCE THEN RETURN "REJECTED: min balance"
        balance ← balance − amount
        APPEND ("WITHDRAW", amount, balance) TO log
        RETURN "accepted"
    END FUNCTION

    REPEAT
        PRINT menu
        READ choice
        CASE choice OF
            "1": READ amount → deposit(amount)   [catch non-numeric]
            "2": READ amount → withdraw(amount)  [catch non-numeric]
            "3": PRINT balance
            "4": FOR (kind, amt, bal) IN log DO PRINT row END FOR
            "5": PRINT summary ; EXIT loop
            DEFAULT: PRINT "unknown option"
        END CASE
    UNTIL choice = "5"
END
```

## Python source code

```python
"""
Case Study 38: ATM Menu-Driven Banking Simulation
--------------------------------------------------
Syllabus: loops (menu loop), conditional statements, operators,
variables, input validation, lists for the transaction log.
"""

MIN_BALANCE = 1000            # balance must never fall below this
MAX_WITHDRAW = 10000          # per-transaction ceiling
MAX_DEPOSIT = 100000          # per-transaction ceiling
OPENING_BALANCE = 5000


def do_deposit(state, amount):
    """Apply a deposit. Returns (ok, message)."""
    if amount <= 0:
        return False, "REJECTED: deposit must be positive."
    if amount > MAX_DEPOSIT:
        return False, "REJECTED: deposit exceeds Rs %d limit." % MAX_DEPOSIT
    state["balance"] += amount
    state["log"].append(("DEPOSIT", amount, state["balance"]))
    return True, "Deposited Rs %.2f. Balance = Rs %.2f" % (amount, state["balance"])


def do_withdraw(state, amount):
    """Apply a withdrawal with all rule checks. Returns (ok, message)."""
    if amount <= 0:
        return False, "REJECTED: withdrawal must be positive."
    if amount % 100 != 0:
        return False, "REJECTED: withdrawal must be a multiple of Rs 100."
    if amount > MAX_WITHDRAW:
        return False, "REJECTED: per-withdrawal limit is Rs %d." % MAX_WITHDRAW
    if state["balance"] - amount < MIN_BALANCE:
        return False, ("REJECTED: would drop below minimum balance Rs %d "
                       "(balance Rs %.2f)." % (MIN_BALANCE, state["balance"]))
    state["balance"] -= amount
    state["log"].append(("WITHDRAW", amount, state["balance"]))
    return True, "Withdrawn Rs %.2f. Balance = Rs %.2f" % (amount, state["balance"])


def show_statement(state):
    print("  ---- MINI STATEMENT ----")
    if not state["log"]:
        print("  No transactions yet.")
    for i in range(len(state["log"])):
        kind, amt, bal = state["log"][i]        # tuple unpacking
        print("  %2d. %-8s Rs %9.2f   balance Rs %9.2f" % (i + 1, kind, amt, bal))
    print("  Current balance: Rs %.2f" % state["balance"])


def menu():
    print("\n  1. Deposit        2. Withdraw")
    print("  3. Check balance  4. Mini statement")
    print("  5. Exit")


def main():
    state = {"balance": OPENING_BALANCE, "log": []}
    print("=" * 56)
    print("  ATM BANKING SIMULATION  (opening balance Rs %.2f)" % OPENING_BALANCE)
    print("=" * 56)

    while True:
        menu()
        choice = input("  Enter choice: ").strip()

        if choice == "1":
            try:
                amount = float(input("  Deposit amount: ").strip())
                _, msg = do_deposit(state, amount)
            except ValueError:
                _, msg = False, "REJECTED: invalid amount (numbers only)."
            print("  " + msg)

        elif choice == "2":
            try:
                amount = float(input("  Withdraw amount: ").strip())
                _, msg = do_withdraw(state, amount)
            except ValueError:
                _, msg = False, "REJECTED: invalid amount (numbers only)."
            print("  " + msg)

        elif choice == "3":
            print("  Current balance: Rs %.2f" % state["balance"])

        elif choice == "4":
            show_statement(state)

        elif choice == "5":
            print("-" * 56)
            print("  SESSION END: %d transaction(s), closing balance Rs %.2f"
                  % (len(state["log"]), state["balance"]))
            print("=" * 56)
            break

        else:
            print("  REJECTED: unknown option '%s' - choose 1-5." % choice)


if __name__ == "__main__":
    main()
```

## Test cases

Ten automated checks: deposit accepted and logged; negative and over-limit deposits rejected; withdrawal accepted; non-multiple of 100, over Rs 10,000 and below the minimum balance all rejected; withdrawal to exactly Rs 1,000 allowed; non-numeric input caught; the log keeps running balances. The scripted demo also exercises three rejections. All pass (test_cases.py).

## Output screenshot

![Output screenshot](output_screenshot.png)

## Conclusion

All five withdrawal rules are checked before any state changes, so every invalid operation leaves the balance untouched while the log doubles as the mini statement through simple tuple unpacking.
