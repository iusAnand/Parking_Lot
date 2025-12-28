import datetime
from models.models import *
from strgy import *
from strgy.getSlotFactory import SlotFactory
from exception.gateNotFound import GateNotFound

class TicketService:

    def __init__(self,GateRepo,VehicleRepo,SlotRepo,ParkingLotRepo,TicketRepo):
        self.gate_repo = GateRepo
        self.vehicle_repo = VehicleRepo
        self.slot_repo = SlotRepo
        self.parking_lot_repo = ParkingLotRepo
        self.ticket_repo = TicketRepo
    #
    def issueTicket(self,vehicle_number: str, owner_name: str, gate_id: int, vehicle_type: str) -> Ticket:
        # issueTicket will return Ticket model object
    
    # create empty ticket
        ticket = Ticket(id=-1,number="",entry_time=datetime.now(),vehicle=None,parking_slot=None,generated_gate=None)
            # empty ticket created ticket object
        
    # set info like gate no
        gate = self.gate_repo.find_gate_by_id(gate_id)
        if gate == None: # if gate not found
            raise GateNotFound("Gate not found")            
        ticket.generated_gate=gate # assign gate to ticket
    #Vehicle info
        vehicle=self.vehicle_repo.find_vehicle_by_number(vehicle_number)
        if vehicle == None:#if vehicle not found create new vehicle
            # create new vehicle object
            vehicle=Vehicle(id=vehicle_number,owner_name=owner_name,vehicle_type=vehicle_type) 
            #save new vehicle to db and get the saved vehicle
            vehicle=self.vehicle_repo.save_vehicle(vehicle) 
        
        ticket.vehicle=vehicle # assign vehicle to ticket
        
    # find the slot using slot strategy
        slotStgy= SlotFactory.get_slot_stgy_obj(gate.parking_lot.slot_assignment_strategy)

        if not slotStgy:
            raise Exception("Slot Strategy not found")
        
        slot=slotStgy.get_slot(vehicle.vehicle_type, gate)
        if not slot:
            raise Exception("No slot available")

        ticket.parking_slot=slot # assign slot to ticket

        # update the slot
        self.slot_repo.update_slot_status(slot, SlotStatus.FILLED)

        # update parking counter

        self.parking_lot_repo.update_parking_lot(gate.parking_lot)

    # return ticket
        return self.ticket_repo.save_ticket(ticket)
       

