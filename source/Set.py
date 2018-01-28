#!python
from hashtable import HashTable

class Set():
    def __init__(self, elements=None):
        '''
        Initialize a new empty set structure and add 
        each element if a sequence is given.
        '''
        self.size = 0
        self.hash = HashTable()
    
    def contains(self, element):
        '''
        return a boolean indicating whether element is
        in this set
        '''
        if self.hash.contains(element):
            return True
        else:
            return False
    
    def add(self, element):
        '''
        Add item to set
        '''
        if self.hash.contains(element):
            return 0
        else:
            self.hash.set(element, True)
            return 0



    def remove(self, element):
        '''
        Remove item from set
        '''
        self.hash.delete(element)
        return 0

    def get_items(self):
        '''
        Get all elements in the set
        '''
        return self.hash.keys()


if __name__ == "__main__":
    print("sets everywhere!")
    car_parts = Set()
    car_parts.add("Smuffler")
    car_parts.add("Noodler")
    car_parts.add("Flanginator")
    car_parts.add("Smuffler")
    print(car_parts.get_items())
    print(car_parts.contains("Noodler"))
    print(car_parts.contains("Roo"))

    