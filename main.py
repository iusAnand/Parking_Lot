from controler.TicketController import TicketController
from dtos.IssueTokenRequest import IssueTokenRequest
from models.models import VehicleType
from repo.GateRepo import GateRepo
from repo.ParkingLotRepo import ParkingLotRepo
from repo.VehicleRepo import VehicleRepo
from strgy.RandomSlotFindingStgy import RandomSlotFindingStgy
from repo.slotRepo import SlotRepo
from repo.ticketRepo import TicketRepo
from service.TicketService import TicketService
from models.models import VehicleType, Gate, GateType, GateStatus, SlotStatus, Slot, FloorStatus, Floor, \
    ParkingLotStatus, \
    SlotAssignmentStrategyEnum, ParkingLot


def setup_initial_data(gate_repo: GateRepo, parking_lot_repo: ParkingLotRepo, slot_repo: SlotRepo):
    # Create ParkingLot
    parking_lot = ParkingLot(
        id=1,
        name="Main Parking Lot",
        address="123 Main St",
        parking_floors=[],
        gates=[],
        allowed_vehicles=[VehicleType.CAR, VehicleType.BIKE],
        capacity=100,
        status=ParkingLotStatus.OPEN,
        slot_assignment_strategy=SlotAssignmentStrategyEnum.RANDOM
    )

    # Create Floor
    floor = Floor(
        id=1,
        parking_slots_list=[],
        floor_number=1,
        floor_status=FloorStatus.OPEN,
        allowed_vehicles=[VehicleType.CAR, VehicleType.BIKE]
    )

    # Create Slots
    slot1 = Slot(
        id=1,
        slot_number=1,
        vehicle_type=VehicleType.CAR,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor
    )

    slot2 = Slot(
        id=2,
        slot_number=2,
        vehicle_type=VehicleType.BIKE,
        parking_slot_status=SlotStatus.EMPTY,
        parking_floor=floor
    )

    # Assign Slots to Floor
    floor.parking_slots_list = [slot1, slot2]

    # Assign Floor to ParkingLot
    parking_lot.parking_floors = [floor]

    # Create Gates
    gate = Gate(
        id=1,
        gate_number=1,
        gate_type=GateType.ENTRY,
        parking_lot=parking_lot,
        gate_status=GateStatus.OPEN
    )

    # Assign Gates to ParkingLot
    parking_lot.gates = [gate]

    # Save to Repositories
    gate_repo.gate_map[gate.id] = gate
    parking_lot_repo.parking_lot[parking_lot.id] = parking_lot
    slot_repo.slots[slot1.id] = slot1
    slot_repo.slots[slot2.id] = slot2




if __name__ == "__main__":
    gate_repo = GateRepo()
    vehicle_repo = VehicleRepo()
    slot_repo = SlotRepo()
    parking_lot_repo = ParkingLotRepo()
    ticket_repo = TicketRepo()
    bill_repo= BillRepo( )
    setup_initial_data(gate_repo, parking_lot_repo, slot_repo)
    
   

    ticket_service = TicketService(gate_repo, vehicle_repo, slot_repo, parking_lot_repo, ticket_repo)

    ticket_controller = TicketController(ticket_service)
# for car
    request = IssueTokenRequest(vehicleNumber="KA-01-HH-1234", ownerName="John Doe", gateId=1,vehicleType=VehicleType.CAR)

    response = ticket_controller.issue_ticket(request)
    print(response)
# for bike
    request = IssueTokenRequest(vehicleNumber="KA-01-HH-123", ownerName="John Doe", gateId=1,vehicleType=VehicleType.BIKE)

    response = ticket_controller.issue_ticket(request)
    print(response)
#to do : Bill-Controller, Bill-service, bill-repo
    bill_service = BillService(ticket_repo, bill_repo)
    bill_controller = BillController(bill_service)

    bill_request = BillReqDto(ticket_id=ticket_response.ticketId)
    bill_response = bill_controller.generate_bill(bill_request)

    print(bill_response)      
   
   
