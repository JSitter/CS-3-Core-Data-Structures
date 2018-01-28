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
        pass
    
    def add(self, element):
        pass

    def remove(self, element):
        pass

if __name__ == "__main__":
    print("sets everywhere!")
    Set()