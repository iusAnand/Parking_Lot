from models.models import VehicleType, Slot, SlotStatus, Gate
from strgy.slotStgy import SlotStgy

class RandomSlotFindingStgy(SlotStgy):

    def get_slot(self, vehicle_type: VehicleType, gate:Gate,) -> Slot:
        # implement random slot finding logic here
        for floor in gate.parking_lot.parking_floors:# iterate through all floors to find this vehicle type allowed or not
            if vehicle_type in floor.allowed_vehicles:# which floor allows this vehicle type
                for slot in floor.parking_slots_list: # iterate through all slots in that floor
                    if slot.vehicle_type == vehicle_type and slot.parking_slot_status == SlotStatus.EMPTY:# check for free slot of that vehicle type
                        return slot 
        return None  # if no slot found