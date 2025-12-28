class LIFOSlotFindingStrategy(SlotFindingStrategy):

    def get_slot(self, vehicle_type, gate):
        stack = gate.parking_lot.free_slots_lifo.get(vehicle_type)

        if not stack:
            return None

        return stack.pop()   # LAST FREE SLOT
