class Vehicle:

    def __init__ (self,color):
        self.color = color

    def getColor(self):
        return self.color
    
    def toString(self):
        return f"This vehicle is {self.getColor()}"
    
if __name__ == '__main__':
    
    vehicle1 = Vehicle("red")

    print(vehicle1.getColor())
    print(vehicle1.toString())
