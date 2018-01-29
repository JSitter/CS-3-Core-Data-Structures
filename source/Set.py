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
        if elements is not None:
            for element in elements:
                self.add(element)
    
    def contains(self, element):
        '''
        return a boolean indicating whether element is
        in this set
        '''
        if self.hash.contains(element):
            return True
        else:
            return False
    
    def add(self, elements):
        '''
        Add item to set
        O(l) where l is the length of the list
        '''

        if isinstance(elements, type([])):
            for element in elements:
                #add item if it doesn't aready exist
                #O(2l) runtrime when l is th length of the linked list
                if not self.hash.contains(element):
                    self.hash.set(element, True)
                    self.size += 1
    

        elif self.hash.contains(elements):
            return 0
        else:
            self.hash.set(elements, True)
            self.size += 1
            return 0

    def remove(self, element):
        '''
        Remove item from set
        '''
        self.hash.delete(element)
        self.size -= 1
        return 0

    def get_items(self):
        '''
        Get all elements in the set
        '''
        return self.hash.keys()
    
    def get_union(self, set_b):
        '''
        Return a set of of self's set and set b
        '''
        print(type(self.get_items()))
        set_a = self.get_items()
        set_c = set_a + set_b

        return set_c
        
    
    def get_intersection(self):
        ''''
        Return a set of the intersection of a and b
        '''
        pass
    
    def get_difference(self):
        '''
        Return a set of A - B
        '''
        pass



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

    