from device import Device
class Laptop(Device):
    def __init__(self,name,price,stock,warranty,ram_size,processor_speed):
        super().__init__(name,price,stock,warranty)
        self.ram_size=ram_size
        self.processor_speed=processor_speed
    
    def __str__(self): 
         return f"Laptop Name:{self.name}\n Price:{self.price}\n Warranty Period:{self.warranty}\n RAM Size:{self.ram_size}\n Processor Speed:{self.processor_speed}"
    
    def run_program(self):
        print("Running a program...")

    def use_keyboard(self):
        print("Typing on the keyboard...")