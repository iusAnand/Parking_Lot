from models.models import ParkingLot

class ParkingLotRepo:
    parking_lot = {}
    def __init__(self):
        self.parking_lot = {}  # key: parking lot id, value: parking lot object
        
    def update_parking_lot(self, parking_lot:ParkingLot):
        parking_lot.capacity = parking_lot.capacity - 1
        self.parking_lot[parking_lot.id] = parking_lot
        return parking_lot