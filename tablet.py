from device import Device
class Tablet(Device):
    def __init__(self,name,price,stock,warranty,screen_resolution,weight):
        super().__init__(name,price,stock,warranty)
        self.screen_resolution=screen_resolution
        self.weight=weight

    def __str__(self): 
         return f"Laptop Name:{self.name}\n Price:{self.price}\n Warranty Period:{self.warranty}\n Screen Resolution:{self.screen_resolution}\n Weight:{self.weight}"
    def browse_internet(self): 
        print("Browsing the Internet...")
    def use_touchscreen(self):
        print("Toching the screen...")