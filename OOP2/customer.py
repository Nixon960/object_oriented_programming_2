class Customer:

    def __init__(self,name,address):
        self.name = name
        self.address = address

    def toString(self):
        return f"Customer Name: {self.name}\nAddress: {self.address}"
    
if __name__=='__main__':
    customer1 = Customer('Nickson','Texas')
    print(customer1.toString())