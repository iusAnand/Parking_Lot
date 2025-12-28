import datetime
from models import Bill, BillStatus



class BillService:
    def __init__(self, TicketRepo, BillRepo):
        self. ticket_repo =TicketRepo
        self. bill_repo= BillRepo
# generate bill

    def generateBill(self, ticket_id: int) -> Bill:

        
        # Checking ticket is present or not
        ticket = self.ticket_repo.find_ticket_by_id(ticket_id)
        if ticket is None:
            raise Exception("Ticket not found")
        # extra entry time from TicketRepo
        entry_time = ticket.entry_time   
        exit_time = datetime.datetime.now()

        duration_minutes = (exit_time - entry_time).total_seconds() / 60
        total_amount = int(duration_minutes * 30)
# create empty Bill for object
        
        bill = Bill(
            id=-1,
            token=ticket_id,
            exit_time=exit_time,
            exited_at=exit_time,
            payments=[],
            total_amount=total_amount,
            bill_status=BillStatus.UNPAID
        )
        return self.bill_repo.save_bill(bill)