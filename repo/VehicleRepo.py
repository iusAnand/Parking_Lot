from models.models import Vehicle


class VehicleRepo:
    
    def __init__(self):
        self.vehicleMap = {}  # vehicle_number to Vehicle object mapping

    # find vehicle by number in db
    def find_vehicle_by_number(self, number):
        if number in self.vehicleMap:# if vehicle found
            return self.vehicleMap[number]
        return None


      
    # if new vehicle save vehicle to db
    def save_vehicle(self, vehicle):
        self.vehicleMap[vehicle.id] = vehicle
        return vehicle


     