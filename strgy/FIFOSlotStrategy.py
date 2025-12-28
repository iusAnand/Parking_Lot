class FIFOSlotFindingStrategy(SlotFindingStrategy):

    def get_slot(self, vehicle_type, gate):
        queue = gate.parking_lot.free_slots_fifo.get(vehicle_type)

        if not queue:
            return None

        return queue.popleft()