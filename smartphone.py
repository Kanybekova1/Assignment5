from device import Device

class Smartphone(Device):
    def __init__(self,name,price,stock,warranty,screen_size,battery_life):
        super().__init__(name,price,stock, warranty)  # Pass only the required 4 arguments
        self.screen_size = screen_size  # Extra attribute
        self.battery_life = battery_life

    def __str__(self):
        return f"Smartphone Name:{self.name}\n Price:{self.price}\n Warranty Period:{self.warranty}\n Screen Size:{self.screen_size}\n Battery Life:{self.battery_life}"

    def make_call(self):
        return f"Smartphone is making a call"

    def install_app(self):
        return f"Install application"