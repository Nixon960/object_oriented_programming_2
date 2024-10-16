
class Garage:

    def __init__(self,parked_Vehicle):
        self.parked_Vehicle = None

    def setVehicle(self,Vehicle):
        self.parked_Vehicle = Vehicle
        return self.parked_Vehicle

    def toString(self):
        if self.parked_Vehicle:
            return f"DEscription of the parked vehicle: {self.parked_Vehicle}"
        else:
            return "The garage is empty"