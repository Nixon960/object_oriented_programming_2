from vehicle_class import Vehicle
from truck import Truck
from garage import Garage

class GarageTester:
    @staticmethod
    def getExample():
        #Create a black Truck without a trailer
        truck = Truck(color="black", trailer=False)

        #create a Garage and park the Truck
        garage = Garage()
        garage.setVehicle(truck)

        print(garage)

