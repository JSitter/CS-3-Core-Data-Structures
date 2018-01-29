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

    def test_union(self):
        car_parts = Set(["Smuffler", "Dongler", "Transplanifier"])
        assert(car_parts.size) is 3
        soup_ing = Set(["Lettuce", "Lentils", "Ginger Snaps", "Tangelos"])
        assert(soup_ing.size) is 4
        new_soup = car_parts.get_union(soup_ing)
        assert(new_soup.size) is 7
    
    def test_intersection(self):
        fridge_parts = Set(["Philistine", "Rodedenrinator", "Turitron", "Coldness"])
        freezer_parts = Set(["Rodedenrinator", "Turitron", "Coldness"])

        boat_parts = fridge_parts.get_intersection(freezer_parts)
        assert(boat_parts.size) is 3
    
    def test_difference(self):
        fridge_parts = Set(["Philistine", "Rodedenrinator", "Turitron", "Coldness"])
        freezer_parts = Set(["Rodedenrinator", "Turitron", "Coldness"])
        accordian_parts = fridge_parts.get_difference(freezer_parts)
        assert(accordian_parts.size) is 1
        assert(accordian_parts.contains("Philistine"))
        sump_parts = freezer_parts.get_difference(fridge_parts)
        assert(sump_parts.size) is 0

if __name__ == "__main__":

    elements = ['one']

    if(isinstance(elements, type([]))):
        print("tis list")
    else:
        print("nope")
