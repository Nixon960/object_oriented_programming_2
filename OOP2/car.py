from vehicle_class import Vehicle

class Car(Vehicle):

    def __init__(self, color,tireType=False):
        super().__init__(color)
        self.tireType = tireType

    def toString(self):
        return f"{super().toString()}\nWinter tires: {self.tireType}"

if __name__ == '__main__':
    
    car1 = Car("blue")
    print(car1.toString())