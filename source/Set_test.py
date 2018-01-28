import unittest
from Set import Set

class set_test(unittest.TestCase):

    def test_set_add(self):
        car_parts = Set()
        car_parts.add("Smuffler")
        assert(car_parts)
        assert(len(car_parts.get_items())) is 1
        car_parts.add("Noodler")
        assert(len(car_parts.get_items())) is 2
        car_parts.add("Smuffler")
        assert(len(car_parts.get_items())) is 2
        assert("Noodler" in car_parts.get_items())
        assert("Smuffler" in car_parts.get_items())
        
