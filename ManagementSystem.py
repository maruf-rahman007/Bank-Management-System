from Bank import Bank
from Admin import Admin
class BankManagementSystem:
    def __init__(self):
        self.bank = Bank()
        self.admin = Admin()
        self.admin.set_bank(self.bank)
        self.logged_in_user = None

    def start(self):
        while True:
            print("\nBank Management System")
            print("1. Register")
            print("2. Login")
            print("3. Admin Login")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.admin_login()
            elif choice == "4":
                print("Exiting the program...")
                break
            else:
                print("Invalid choice. Please try again.")

    def register(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        user = self.bank.create_user(email, password)
        if user:
            print(f"Registration successful. User email: {user['email']}")
        else:
            print("Registration failed.")

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        user = self.bank.get_user_by_email(email)
        if user and user["password"] == password:
            print(f"Login successful. Welcome, {user['email']}!")
            self.logged_in_user = user
            self.user_menu()
        else:
            print("Invalid email or password.")

    def user_menu(self):
        while True:
            print("\nUser Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Transaction History")
            print("6. Request Loan")
            print("7. Check Loan Availability")
            print("8. Check Maximum Loan Amount")
            print("9. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.transfer()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                self.transaction_history()
            elif choice == "6":
                self.request_loan()
            elif choice == "7":
                self.check_loan_availability()
            elif choice == "8":
                self.check_max_loan_amount()
            elif choice == "9":
                print("Logging out...")
                self.logged_in_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if self.bank.deposit(self.logged_in_user, amount):
            print("Deposit successful.")
        else:
            print("Deposit failed.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if self.bank.withdraw(self.logged_in_user, amount):
            print("Withdrawal successful.")
        else:
            print("Withdrawal failed.")

    def transfer(self):
        recipient_email = input("Enter the recipient's email: ")
        recipient = self.bank.get_user_by_email(recipient_email)
        if not recipient:
            print("Recipient not found.")
            return

        amount = float(input("Enter the amount to transfer: "))
        if self.bank.transfer(self.logged_in_user, recipient, amount):
            print("Transfer successful.")
        else:
            print("Transfer failed.")

    def check_balance(self):
        balance = self.logged_in_user["balance"]
        print(f"Your balance: {balance} taka")

    def transaction_history(self):
        history = self.bank.get_transaction_history(self.logged_in_user)
        if not history:
            print("No transaction history available.")
        else:
            print("Transaction History:")
            for transaction in history:
                print(f"Type: {transaction['type']}")
                print(f"Amount: {transaction['amount']} taka")
                if "recipient" in transaction:
                    print(f"Recipient: {transaction['recipient']}")
                if "sender" in transaction:
                    print(f"Sender: {transaction['sender']}")
                print("------")

    def request_loan(self):
        request = self.bank.request_loan(self.logged_in_user)
        if request:
            print("Loan request submitted.")
        else:
            print("Loan request failed.")

    def check_loan_availability(self):
        self.bank.check_loan_availability()

    def check_max_loan_amount(self):
        self.bank.check_max_loan_amount(self.logged_in_user)

    def admin_login(self):
        password = input("Enter admin password: ")
        if password == "admin123":
            print("Admin login successful.")
            self.admin_menu()
        else:
            print("Admin login failed.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu")
            print("1. View Loan Requests")
            print("2. Accept Loan Request")
            print("3. Check Available Balance")
            print("4. Check Total Loan")
            print("5. Turn On Loan Feature")
            print("6. Turn Off Loan Feature")
            print("7. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_loan_requests()
            elif choice == "2":
                self.accept_loan_request()
            elif choice == "3":
                self.check_available_balance()
            elif choice == "4":
                self.check_total_loan()
            elif choice == "5":
                self.turn_on_loan_feature()
            elif choice == "6":
                self.turn_off_loan_feature()
            elif choice == "7":
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def view_loan_requests(self):
        self.admin.view_loan_requests()

    def accept_loan_request(self):
        self.admin.accept_loan_request()

    def check_available_balance(self):
        self.bank.check_available_balance()

    def check_total_loan(self):
        self.bank.check_total_loan()

    def turn_on_loan_feature(self):
        self.bank.loan_available = True
        print("Loan feature is now available.")

    def turn_off_loan_feature(self):
        self.bank.loan_available = False
        print("Loan feature is now disabled.")


