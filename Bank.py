class Bank:
    def __init__(self):
        self.users = []
        self.available_balance = 0
        self.total_loan = 0
        self.loan_available = True
        self.loan_requests = []

    def create_user(self, email, password):
        user = {"email": email, "password": password, "balance": 0, "transaction_history": []}
        self.users.append(user)
        return user

    def get_user_by_email(self, email):
        for user in self.users:
            if user["email"] == email:
                return user
        return None

    def deposit(self, user, amount):
        if amount < 1:
            print("Deposit amount should be at least 1 taka.")
            return False

        user["balance"] += amount
        self.available_balance += amount

        transaction = {
            "type": "Deposit",
            "amount": amount
        }
        user["transaction_history"].append(transaction)

        return True

    def withdraw(self, user, amount):
        if amount < 1:
            print("Withdrawal amount should be at least 1 taka.")
            return False

        if user["balance"] < amount:
            print("Insufficient balance.")
            return False

        user["balance"] -= amount
        self.available_balance -= amount

        transaction = {
            "type": "Withdrawal",
            "amount": amount
        }
        user["transaction_history"].append(transaction)

        return True

    def transfer(self, sender, receiver, amount):
        if amount < 1:
            print("Transfer amount should be at least 1 taka.")
            return False

        if sender["balance"] < amount:
            print("Insufficient balance.")
            return False

        sender["balance"] -= amount
        receiver["balance"] += amount

        sender_transaction = {
            "type": "Transfer Sent",
            "amount": amount,
            "recipient": receiver["email"]
        }
        receiver_transaction = {
            "type": "Transfer Received",
            "amount": amount,
            "sender": sender["email"]
        }

        sender["transaction_history"].append(sender_transaction)
        receiver["transaction_history"].append(receiver_transaction)

        return True

    def get_transaction_history(self, user):
        return user["transaction_history"]

    def request_loan(self, user):
        if not self.loan_available:
            print("Loan feature is currently disabled.")
            return False

        max_loan_amount = user["balance"] * 2
        if self.available_balance >= max_loan_amount:
            transaction = {
                "type": "Loan Request",
                "user": user,
                "amount": max_loan_amount,
                "status": "Pending"
            }
            self.loan_requests.append(transaction)
            return transaction
        else:
            print("Bank does not have sufficient funds to issue the loan.")
            return False

    def check_loan_availability(self):
        if self.loan_available:
            print("Loan feature is currently available.")
        else:
            print("Loan feature is currently disabled.")

    def check_max_loan_amount(self, user):
        max_loan_amount = user["balance"] * 2
        print(f"Maximum loan amount available for you: {max_loan_amount} taka")

    def stop_loan_feature(self):
        self.loan_available = False

    def get_loan_requests(self):
        return self.loan_requests

    def accept_loan_request(self, request):
        if request["status"] == "Pending":
            request["status"] = "Accepted"
            user = request["user"]
            loan_amount = request["amount"]

            user["balance"] += loan_amount
            self.available_balance -= loan_amount

            transaction = {
                "type": "Loan Disbursement",
                "amount": loan_amount
            }
            user["transaction_history"].append(transaction)

            self.total_loan += loan_amount

            print(f"Loan request accepted for user {user['email']}.")
        else:
            print("Loan request is already processed.")

    def check_available_balance(self):
        print(f"Available balance: {self.available_balance} taka")

    def check_total_loan(self):
        print(f"Total loan amount: {self.total_loan} taka")