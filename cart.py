from device import Device
class Cart:
    def __init__(self):
        self.items=[]
        self.total_price=0

    def add_device(self,device,amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            return f"Added {amount} x {device.name} to cart."
        return "Not enough stock available."
    
    def remove_device(self, device, amount):
        pair=(device,amount)

    def get_total_price(self):
        return f"Total price:{self.total_price}" 
    
    def print_items(self):
        for pair in self.items:
            device=pair[0]
            amount=pair[1]
            print(device,"Amount: ",amount)

    def checkout(self):
        if not self.items:
            return "Cart is empty. Add items before checkout."
    
        print("Receipt:")
        for device, amount in self.items:
            print(f"{device.name} - {amount} x ${device.price} = ${device.price * amount}")
        
        print(f"Total Price: ${self.total_price}")
        self.items.clear()
        self.total_price = 0
        return "Checkout complete. Thank you for shopping!"
