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
