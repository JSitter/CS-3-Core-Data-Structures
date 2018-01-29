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
        computer_parts = Set(['Ycombinator', 'North Shore', 'East Bridge'])
        assert(len(computer_parts.get_items())) is 3
        assert(computer_parts.size) is 3
        assert(computer_parts.contains("North Shore"))
        car_parts.add(['one'])
        assert(car_parts.size) is 3


    def test_set_remove(self):
        car_parts = Set()
        car_parts.add("Smuffler")
        car_parts.add("Turbidity Turbine")
        car_parts.add("Rolfoganger")
        car_parts.remove("Rolfoganger")
        assert(len(car_parts.get_items())) is 2
        with self.assertRaises(KeyError):
            car_parts.remove("Fluffykins")
    
    def test_set_contains(self):
        car_parts = Set()
        car_parts.add("Demogorgan")
        car_parts.add("Slurmatron")
        assert(car_parts.contains("Slurmatron"))
        assert(not car_parts.contains("Sluggo"))

if __name__ == "__main__":

    elements = ['one']

    if(isinstance(elements, type([]))):
        print("tis list")
    else:
        print("nope")
