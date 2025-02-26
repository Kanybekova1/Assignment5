class Device:
    def __init__(self,name,price,stock,warranty):
        self.name=name
        self.price=price
        self.stock=stock
        self.warranty=warranty

    def display_info(self):
        return f" Device Name:{self.name}\n Price:{self.price}\n Warranty Period:{self.warranty}"
    def __str__(self):
        return self.display_info()

    def apply_discount(self,discount_percentage):
        self.price=self.price-self.price*discount_percentage/100

    def is_available(self,amount):
        if self.stock>=amount:
            return True
        return False
        
    def reduce_stock(self,amount):
        self.stock=self.stock-amount
        return self.stock


    