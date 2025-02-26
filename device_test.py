import unittest
from cart import Cart
from device import Device
from smartphone import Smartphone
from tablet import Tablet
from laptop import Laptop

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.phone = Smartphone("iPhone 13", 999, 10, 12, 6.1, 20)
        self.laptop = Laptop("MacBook Pro", 1999, 5, 24, 16, 3.2)
        self.tablet = Tablet("iPad Pro", 1299, 7, 18, "2388x1668", 600)
        self.cart = Cart()

    def test_device(self):
        self.assertEqual(self.phone.name, "iPhone 13")
        self.assertEqual(self.laptop.price, 1999)
        self.assertEqual(self.tablet.stock, 7)
        self.assertEqual(self.phone.battery_life, 20)
    
    def test_is_available(self):
        self.assertTrue(self.phone.is_available(5)) 
        self.assertFalse(self.laptop.is_available(10))
    
    def test_add_device(self):
        result = self.cart.add_device(self.phone, 2)
        self.assertEqual(result, "Added 2 x iPhone 13 to cart.")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.total_price, 999 * 2)

    def test_remove_device(self):
       pass
    
    def test_checkout(self):
        self.cart.add_device(self.phone, 2)
        self.cart.checkout()
        self.assertEqual(self.phone.stock, 8)

    def test_apply_discount(self):
        """Test applying discounts on a device."""
        self.phone.apply_discount(10)  # 10% discount
        self.assertEqual(self.phone.price, 899.10) 

if __name__ == '__main__':
    unittest.main()

