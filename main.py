from cart import Cart
from device import Device
from smartphone import Smartphone
from tablet import Tablet
from laptop import Laptop

def create_devices():
    return [
        Smartphone("iPhone 14", 999, 10, 2, "6.1 inches", "20 hours"),
        Smartphone("Samsung Galaxy S21", 799, 12, 1, "6.2 inches", "18 hours"),
        Smartphone("Google Pixel 6", 599, 8, 2, "6.4 inches", "24 hours"),
        Smartphone("OnePlus 9", 729, 15, 1, "6.55 inches", "22 hours"),
        Smartphone("Xiaomi Mi 11", 699, 5, 2, "6.81 inches", "21 hours"),
        Smartphone("Sony Xperia 5 III", 999, 4, 1, "6.1 inches", "25 hours"),
        Smartphone("Motorola Edge Plus", 699, 9, 3, "6.7 inches", "26 hours"),
        Smartphone("Asus ROG Phone 5", 999, 6, 2, "6.78 inches", "30 hours"),
        Smartphone("Nokia XR20", 499, 10, 3, "6.67 inches", "48 hours"),
        Smartphone("Realme GT Neo 3", 599, 7, 1, "6.7 inches", "23 hours"),

        Tablet("iPad Pro", 1099, 7, 2, "2388 x 1668", "1.03 kg"),
        Tablet("Samsung Galaxy Tab S8", 699, 10, 1, "2800 x 1752", "0.7 kg"),
        Tablet("Lenovo Tab P11", 249, 12, 1, "2000 x 1200", "0.49 kg"),
        Tablet("Amazon Fire HD 10", 149, 20, 1, "1920 x 1200", "0.465 kg"),
        Tablet("Microsoft Surface Pro 8", 1299, 6, 2, "2880 x 1920", "0.89 kg"),
        Tablet("Huawei MatePad Pro", 599, 8, 2, "2560 x 1600", "0.46 kg"),
        Tablet("Google Pixel Slate", 899, 5, 2, "3000 x 2000", "0.725 kg"),

        Laptop("MacBook Pro", 1999, 5, 2, "16GB", "3.1 GHz"),
        Laptop("Dell XPS 13", 1399, 10, 2, "16GB", "3.9 GHz"),
        Laptop("HP Spectre x360", 1599, 7, 2, "16GB", "4.1 GHz"),
        Laptop("Asus ROG Zephyrus G14", 1499, 8, 1, "32GB", "4.4 GHz"),
        Laptop("Acer Swift 3", 799, 15, 1, "8GB", "3.6 GHz"),
        Laptop("Razer Blade 15", 2499, 3, 2, "32GB", "5.0 GHz"),
        Laptop("MSI Stealth 15M", 1799, 6, 2, "16GB", "4.8 GHz")
    ]

    
    
def show_devices(devices):
    print("\nAvailable Devices:")
    
    for index in range(len(devices)): 
        device = devices[index]
        print(f"{index + 1}. Name: {device.name}, Price: ${device.price}, Stock: {device.stock}") 
    
def main():
    devices = create_devices()
    cart = []

    while True:
        print("\nMenu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")

        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            show_devices(devices)
            device_choice = int(input("\nSelect a device to add to cart (or 0 to cancel): "))
            if device_choice > 0 and device_choice <= len(devices):
                device = devices[device_choice - 1]
                if device.stock > 0:
                    cart.append(device)
                    device.stock -= 1
                    print(f"{device.name} added to cart.")
                else:
                        print("Sorry, this device is out of stock.")
            elif device_choice == 0:
                    continue
            else:
                    print("Invalid selection.")

        elif choice == '2':
                if not cart:
                    print("Your cart is empty.")
                else:
                    print("\nYour Cart:")
                    for item in cart:
                        print(item)
            
        elif choice == '3':
                print("Exiting the program. Thank you!")
                break
            
        else:
                print("Invalid selection. Please try again.")
if __name__ == "__main__":
    main()           