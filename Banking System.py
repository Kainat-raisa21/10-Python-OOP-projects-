class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount:.2f}"


class Account:
    def __init__(self, account_no, holder_name, contact, balance=0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.contact = contact
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(Transaction("Deposit", amount))
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.balance >= amount:  # Fixed condition to allow full balance withdrawal
            self.balance -= amount
            self.transaction_history.append(Transaction("Withdraw", amount))
            print(f"Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        return self.balance

    def print_statement(self):
        print(f"Account Statement for {self.holder_name} (Account No: {self.account_no})")
        for transaction in self.transaction_history:
            print(transaction)
        print(f"Current Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}
        self.next_account_number = 1001

    def create_account(self, holder_name, contact, balance=0):
        account_no = self.next_account_number
        new_account = Account(account_no, holder_name, contact, balance)
        self.accounts[account_no] = new_account
        print(f"Account created for {holder_name}. Account number: {account_no}")
        self.next_account_number += 1
        return new_account

    def find_account(self, account_no):
        return self.accounts.get(account_no)

    def fund_transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account:
            if from_account.check_balance() >= amount:  # Fixed condition for transfer
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount:.2f} from Account {from_account_number} to Account {to_account_number}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid account number(s) for transfer.")


if __name__ == "__main__":
    bank = Bank("Swiss Bank")

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Funds")
        print("6. Print Account Statement")
        print("7. Exit")

        choice = int(input("Choose an option (enter a number): "))

        if choice == 1:
            name = input("Enter account holder name: ")
            contact = input("Enter contact information: ")  # Added input for contact
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, contact, initial_balance)  # Passed contact to method
        elif choice == 2:
            acc_no = int(input("Enter your account number: "))
            depo_amount = float(input("Enter deposit amount: "))
            acc = bank.find_account(acc_no)
            if acc:
                acc.deposit(depo_amount)
            else:
                print("Account not found.")
        elif choice == 3:
            acc_no = int(input("Enter your account number: "))
            with_amount = float(input("Enter withdrawal amount: "))
            acc = bank.find_account(acc_no)
            if acc:
                acc.withdraw(with_amount)  # Fixed method call to withdraw
            else:
                print("Account not found.")
        elif choice == 4:
            acc_no = int(input("Enter your account number: "))
            acc = bank.find_account(acc_no)
            if acc:
                print(f"Your balance is: ${acc.check_balance():.2f}")
            else:
                print("Account not found.")
        elif choice == 5:
            from_acc_no = int(input("Enter the account number you want to transfer funds 'FROM': "))
            to_acc_no = int(input("Enter the account number you want to transfer funds 'TO': "))
            amount = float(input("Enter transferable amount: "))
            bank.fund_transfer(from_acc_no, to_acc_no, amount)
        elif choice == 6:
            acc_no = int(input("Enter your account number: "))
            acc = bank.find_account(acc_no)
            if acc:
                acc.print_statement()
            else:
                print("Account not found.")
        elif choice == 7:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
