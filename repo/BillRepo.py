# repo/BillRepo.py
class BillRepo:
    def __init__(self):
        self.bills = {}

    def save_bill(self, bill):
        self.bills[bill.id] = bill
        return bill

    def get_by_id(self, bill_id):
        return self.bills.get(bill_id)
