"""
Banking Management System — OOP Lab Exercise
Demonstrates: classes/objects, __init__, instance & class variables,
encapsulation, inheritance, super(), method overriding, multiple
inheritance (mixin), abstract classes/methods, polymorphism, duck typing,
and class relationships (composition, aggregation, association).

Run:  python bank_system.py          -> scripted demo
      python bank_system.py --menu   -> interactive menu
"""

from abc import ABC, abstractmethod
from datetime import datetime
import sys


# ---------------------------------------------------------------
# Custom exception (reusable error type for the whole application)
# ---------------------------------------------------------------
class InsufficientFundsError(Exception):
    pass


# ---------------------------------------------------------------
# Transaction: a small reusable value class
# ---------------------------------------------------------------
class Transaction:
    def __init__(self, kind, amount, balance_after):
        self.kind = kind
        self.amount = amount
        self.balance_after = balance_after
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.time}  {self.kind:<12} {self.amount:>10.2f}  bal: {self.balance_after:>10.2f}"


# ---------------------------------------------------------------
# Abstract base class
# ---------------------------------------------------------------
class Account(ABC):
    bank_name = "PyBank"          # class variable (shared by all accounts)
    _next_number = 1001           # class variable used to generate IDs

    def __init__(self, owner, balance=0.0):
        self.account_no = Account._next_number   # instance variables
        Account._next_number += 1
        self.owner = owner                       # association with Customer
        self._balance = balance                  # "protected" by convention
        self.transactions = []                   # composition: account owns its transactions
        if balance > 0:
            self._record("OPENING", balance)

    # read-only property -> encapsulation
    @property
    def balance(self):
        return self._balance

    def _record(self, kind, amount):
        self.transactions.append(Transaction(kind, amount, self._balance))

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self._record("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.available_funds():
            raise InsufficientFundsError(
                f"Account {self.account_no}: cannot withdraw {amount:.2f}")
        self._balance -= amount
        self._record("WITHDRAW", amount)

    def available_funds(self):
        return self._balance

    @abstractmethod
    def account_type(self):
        """Every concrete account must say what kind it is."""

    @abstractmethod
    def month_end(self):
        """Every concrete account must define its month-end processing."""

    def statement(self):
        lines = [f"--- {self.bank_name} statement: {self.account_type()} "
                 f"#{self.account_no} ({self.owner.name}) ---"]
        lines += [str(t) for t in self.transactions]
        lines.append(f"Current balance: {self._balance:.2f}")
        return "\n".join(lines)

    def __str__(self):
        return f"{self.account_type():<8} #{self.account_no}  {self.owner.name:<10} {self._balance:>10.2f}"


# ---------------------------------------------------------------
# Mixin (used for multiple inheritance)
# ---------------------------------------------------------------
class InterestMixin:
    interest_rate = 0.0   # annual rate; overridden by subclasses

    def add_interest(self):
        interest = round(self._balance * self.interest_rate / 12, 2)
        if interest > 0:
            self._balance += interest
            self._record("INTEREST", interest)
        return interest


# ---------------------------------------------------------------
# Concrete child classes
# ---------------------------------------------------------------
class SavingsAccount(InterestMixin, Account):     # multiple inheritance
    interest_rate = 0.04
    MIN_BALANCE = 500

    def __init__(self, owner, balance=0.0, withdrawals_per_month=5):
        super().__init__(owner, balance)          # call parent __init__
        self.withdrawals_per_month = withdrawals_per_month
        self.withdrawals_this_month = 0

    def account_type(self):
        return "Savings"

    def available_funds(self):                    # method overriding
        return self._balance - self.MIN_BALANCE

    def withdraw(self, amount):                   # override + extend with super()
        if self.withdrawals_this_month >= self.withdrawals_per_month:
            raise InsufficientFundsError("Monthly withdrawal limit reached")
        super().withdraw(amount)
        self.withdrawals_this_month += 1

    def month_end(self):
        self.withdrawals_this_month = 0
        return f"interest added {self.add_interest():.2f}"


class CurrentAccount(Account):
    def __init__(self, owner, balance=0.0, overdraft_limit=10000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self):
        return "Current"

    def available_funds(self):                    # overdraft allowed
        return self._balance + self.overdraft_limit

    def month_end(self):
        if self._balance < 0:
            fee = 200
            self._balance -= fee
            self._record("OD FEE", fee)
            return f"overdraft fee charged {fee:.2f}"
        return "no charges"


class FixedDeposit(InterestMixin, Account):
    interest_rate = 0.07

    def account_type(self):
        return "FD"

    def withdraw(self, amount):
        raise InsufficientFundsError("Fixed deposits cannot be withdrawn before maturity")

    def month_end(self):
        return f"interest added {self.add_interest():.2f}"


# ---------------------------------------------------------------
# Customer: has many accounts (association)
# ---------------------------------------------------------------
class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.accounts = []

    def total_balance(self):
        return sum(a.balance for a in self.accounts)

    def __str__(self):
        return f"{self.customer_id}: {self.name} ({len(self.accounts)} accounts)"


# ---------------------------------------------------------------
# Bank: the application's controller (aggregates customers & accounts)
# ---------------------------------------------------------------
class Bank:
    ACCOUNT_TYPES = {"savings": SavingsAccount,
                     "current": CurrentAccount,
                     "fd": FixedDeposit}

    def __init__(self, name):
        self.name = name
        self.customers = {}
        self.accounts = {}

    def add_customer(self, name, phone):
        cid = f"C{len(self.customers) + 1:03d}"
        customer = Customer(cid, name, phone)
        self.customers[cid] = customer
        return customer

    def open_account(self, customer, kind, initial=0.0):
        cls = self.ACCOUNT_TYPES[kind.lower()]    # factory: pick a class by name
        account = cls(customer, initial)
        customer.accounts.append(account)
        self.accounts[account.account_no] = account
        return account

    def find(self, account_no):
        try:
            return self.accounts[account_no]
        except KeyError:
            raise ValueError(f"No account #{account_no}") from None

    def transfer(self, from_no, to_no, amount):
        src, dst = self.find(from_no), self.find(to_no)
        src.withdraw(amount)        # raises if not allowed -> nothing changes
        dst.deposit(amount)

    def run_month_end(self):
        # Polymorphism: same call, each class behaves differently
        for acc in self.accounts.values():
            print(f"  #{acc.account_no} {acc.account_type():<8}: {acc.month_end()}")

    def report(self):
        print(f"\n===== {self.name} — all accounts =====")
        for acc in self.accounts.values():
            print(" ", acc)
        print(f"  Total deposits held: {sum(a.balance for a in self.accounts.values()):.2f}")


# ---------------------------------------------------------------
# Duck typing: works with ANY object that has a .statement() method
# ---------------------------------------------------------------
class LoanRecord:   # not an Account at all — unrelated class
    def __init__(self, owner, amount):
        self.owner, self.amount = owner, amount

    def statement(self):
        return f"--- Loan for {self.owner.name}: outstanding {self.amount:.2f} ---"


def print_statements(items):
    for item in items:
        print(item.statement())   # no isinstance() check needed
        print()


# ---------------------------------------------------------------
# Demo and interactive menu
# ---------------------------------------------------------------
def demo():
    bank = Bank("PyBank Bhopal Branch")
    asha = bank.add_customer("Asha", "98260xxxxx")
    ravi = bank.add_customer("Ravi", "94250xxxxx")

    s1 = bank.open_account(asha, "savings", 20000)
    c1 = bank.open_account(ravi, "current", 5000)
    fd = bank.open_account(asha, "fd", 100000)

    s1.deposit(5000)
    s1.withdraw(3000)
    c1.withdraw(12000)                 # uses overdraft -> negative balance
    bank.transfer(s1.account_no, c1.account_no, 2000)

    for attempt in (lambda: fd.withdraw(100),
                    lambda: s1.withdraw(1_000_000)):
        try:
            attempt()
        except InsufficientFundsError as e:
            print("Blocked:", e)

    bank.report()
    print("\nMonth-end processing (polymorphism):")
    bank.run_month_end()
    bank.report()

    print("\nDuck typing — statements from unrelated classes:\n")
    print_statements([s1, c1, LoanRecord(ravi, 250000)])

    print("Can we instantiate the abstract class?")
    try:
        Account(asha)
    except TypeError as e:
        print("  No:", e)

    print("\nMRO of SavingsAccount:", [k.__name__ for k in SavingsAccount.__mro__])


def menu():
    bank = Bank("PyBank")
    actions = """
1. Add customer        2. Open account     3. Deposit
4. Withdraw            5. Transfer         6. Statement
7. All accounts        8. Month end        0. Exit
"""
    while True:
        print(actions)
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                c = bank.add_customer(input("Name: "), input("Phone: "))
                print("Created", c)
            elif choice == "2":
                c = bank.customers[input("Customer ID (e.g. C001): ").strip()]
                kind = input("Type (savings/current/fd): ")
                a = bank.open_account(c, kind, float(input("Initial amount: ")))
                print("Opened", a)
            elif choice == "3":
                bank.find(int(input("Account no: "))).deposit(float(input("Amount: ")))
                print("Done")
            elif choice == "4":
                bank.find(int(input("Account no: "))).withdraw(float(input("Amount: ")))
                print("Done")
            elif choice == "5":
                bank.transfer(int(input("From: ")), int(input("To: ")), float(input("Amount: ")))
                print("Done")
            elif choice == "6":
                print(bank.find(int(input("Account no: "))).statement())
            elif choice == "7":
                bank.report()
            elif choice == "8":
                bank.run_month_end()
            elif choice == "0":
                break
            else:
                print("Invalid choice")
        except (ValueError, KeyError, InsufficientFundsError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu() if "--menu" in sys.argv else demo()
