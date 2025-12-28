class SlotRepo:
    slots={}
    def __init__(self):
        # by me
        self.slots={} # key:slot id , value: slot object

    def update_slot_status(self,slot, status):
        slot.parking_slot_status = status
        self.slots[slot.id] = slot
        return slot