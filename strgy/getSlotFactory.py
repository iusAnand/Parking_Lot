from models.models import SlotAssignmentStrategyEnum
from strgy.RandomSlotFindingStgy import RandomSlotFindingStgy

class SlotFactory:
    @staticmethod # why static method: because we don't need to create an instance of SlotFactory to use this method
    def get_slot_stgy_obj(slotStrgyEnum):
        # for random strategy is implemented
        if slotStrgyEnum == SlotAssignmentStrategyEnum.RANDOM:
            return RandomSlotFindingStgy()
        # for LIFO strategy
        if slotStrgyEnum == SlotAssignmentStrategyEnum.LIFO:
            return LIFOSlotFindingStgy()
        # for FIFO strategy
        if slotStrgyEnum == SlotAssignmentStrategyEnum.FIFO:
            return FIFOSlotFindingStgy()
            