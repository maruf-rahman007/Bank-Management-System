class Admin:
    def __init__(self):
        self.bank = None

    def set_bank(self, bank):
        self.bank = bank

    def view_loan_requests(self):
        loan_requests = self.bank.get_loan_requests()
        print("Loan Requests:")
        for request in loan_requests:
            user = request["user"]
            print(f"User: {user['email']}")
            print(f"Amount: {request['amount']} taka")
            print(f"Status: {request['status']}")
            print("------")

    def accept_loan_request(self):
        loan_requests = self.bank.get_loan_requests()
        if not loan_requests:
            print("No loan requests available.")
            return

        self.view_loan_requests()

        request_index = int(input("Enter the index of the loan request to accept: "))
        if request_index < 0 or request_index >= len(loan_requests):
            print("Invalid loan request index.")
            return

        request = loan_requests[request_index]
        self.bank.accept_loan_request(request)