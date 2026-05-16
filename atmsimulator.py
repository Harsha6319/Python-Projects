import json
import os

DATA_FILE = "accounts.json"

# ---------------------------
# Helper functions
# ---------------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------
# ATM Class
# ---------------------------
class ATM:
    def __init__(self):
        self.accounts = load_data()
        self.next_acc_no = self.get_next_account_no()

    def get_next_account_no(self):
        if not self.accounts:
            return 1001
        return max(map(int, self.accounts.keys())) + 1

    def create_account(self):
        name = input("Enter name: ")
        pin = input("Set 4-digit PIN: ")
        initial = float(input("Initial deposit: "))

        acc_no = str(self.next_acc_no)
        self.accounts[acc_no] = {
            "name": name,
            "pin": pin,
            "balance": initial,
            "transactions": []
        }

        save_data(self.accounts)

        print("\nAccount created successfully!")
        print(f"Your account number is: {acc_no}\n")

        self.next_acc_no += 1

    def login(self):
        acc_no = input("Enter account number: ")
        pin = input("Enter PIN: ")

        if acc_no in self.accounts and self.accounts[acc_no]["pin"] == pin:
            print(f"\nWelcome {self.accounts[acc_no]['name']}!\n")
            self.user_menu(acc_no)
        else:
            print("Invalid account number or PIN.\n")

    # ---------------------------
    # User Functions
    # ---------------------------
    def check_balance(self, acc_no):
        bal = self.accounts[acc_no]["balance"]
        print(f"Balance = ₹{bal}\n")

    def deposit(self, acc_no):
        amt = float(input("Amount to deposit: "))
        self.accounts[acc_no]["balance"] += amt
        self.accounts[acc_no]["transactions"].append(f"Deposited ₹{amt}")
        save_data(self.accounts)
        print("Deposit successful!\n")

    def withdraw(self, acc_no):
        amt = float(input("Amount to withdraw: "))
        if amt <= self.accounts[acc_no]["balance"]:
            self.accounts[acc_no]["balance"] -= amt
            self.accounts[acc_no]["transactions"].append(f"Withdrew ₹{amt}")
            save_data(self.accounts)
            print("Withdrawal successful!\n")
        else:
            print("Insufficient balance!\n")

    def transfer(self, acc_no):
        to_acc = input("Enter destination account: ")
        if to_acc not in self.accounts:
            print("Account not found.\n")
            return

        amt = float(input("Amount to transfer: "))

        if amt <= self.accounts[acc_no]["balance"]:
            self.accounts[acc_no]["balance"] -= amt
            self.accounts[to_acc]["balance"] += amt

            self.accounts[acc_no]["transactions"].append(f"Transferred ₹{amt} to {to_acc}")
            self.accounts[to_acc]["transactions"].append(f"Received ₹{amt} from {acc_no}")

            save_data(self.accounts)
            print("Transfer successful!\n")
        else:
            print("Insufficient balance!\n")

    def mini_statement(self, acc_no):
        print("\nLast 5 transactions:")
        txns = self.accounts[acc_no]["transactions"][-5:]
        if not txns:
            print("No transactions yet.\n")
        else:
            for t in txns:
                print("-", t)
            print()

    def change_pin(self, acc_no):
        old = input("Enter old PIN: ")
        if old != self.accounts[acc_no]["pin"]:
            print("Incorrect old PIN.\n")
            return
        new = input("Enter new PIN: ")
        self.accounts[acc_no]["pin"] = new
        save_data(self.accounts)
        print("PIN changed successfully!\n")

    # ---------------------------
    # User Menu
    # ---------------------------
    def user_menu(self, acc_no):
        while True:
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Mini Statement")
            print("6. Change PIN")
            print("0. Logout")

            ch = input("Choose: ")

            if ch == "1":
                self.check_balance(acc_no)
            elif ch == "2":
                self.deposit(acc_no)
            elif ch == "3":
                self.withdraw(acc_no)
            elif ch == "4":
                self.transfer(acc_no)
            elif ch == "5":
                self.mini_statement(acc_no)
            elif ch == "6":
                self.change_pin(acc_no)
            elif ch == "0":
                print("Logged out.\n")
                break
            else:
                print("Invalid choice.\n")


# ---------------------------
# Main Program
# ---------------------------
atm = ATM()

while True:
    print("=== ATM SYSTEM (Intermediate) ===")
    print("1. Create Account")
    print("2. Login")
    print("0. Exit")

    ch = input("Choose: ")

    if ch == "1":
        atm.create_account()
    elif ch == "2":
        atm.login()
    elif ch == "0":
        print("Thank you!")
        break
    else:
        print("Invalid choice.\n")
