from dtos import BillResponseDTO
from dtos import BillReqDto
from services import BillService


class BillController:
    def __init__(self,billService: BillService ):
        self. billService=billService
        

    def generate_bill(self, request: BillReqDto) -> BillResponseDTO:

        bill=self.billService.generateBill(request.ticket_id)

        response=BillResponseDTO()
        response = BillResponseDTO()
        response.ticket_id = bill.token
        response.bill_id = bill.id
        response.exit_time = bill.exited_at
        response.total_amount = bill.total_amount
        response.bill_status = bill.bill_status

        return response


       

        