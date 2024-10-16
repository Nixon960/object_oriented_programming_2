from vehicle_class import Vehicle

class Truck(Vehicle):

    def __init__(self, color,trailer=False):
        super().__init__(color)
        self.trailer = trailer

    def toString(self):
        return f"{super().toString()}\nhas trailer: {self.trailer}"
    
if __name__ == '__main__':

    Truck1 = Truck("red")
    print(Truck1.toString())