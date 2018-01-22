#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.size == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item
        self.list.prepend(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.list.size == 0:
            return None
        else:
            return self.list.get_at_index(self.list.size - 1)

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any

        if self.list.size == 0:
            raise ValueError("Queue is empty")
        
        if self.list.size == 1:
            return_value = self.list.head.data
            self.list.delete(return_value)
            return return_value

        previous_node = self.list.head

        for _ in range(0, self.list.size - 2):
            previous_node = previous_node.next

        return_value = previous_node.next.data
        self.list.tail = previous_node
        previous_node.next = None
        self.list.size -= 1
        return return_value

        



# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        # TODO: Check if empty
        if self.length() > 0:
            return False
        else:
            return True



    def length(self):
        """Return the number of items in this queue."""
        # TODO: Count number of items
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(n) – Why? 
        The thing has to create a new array and copy all n elements over"""
        # TODO: Insert given item

        new_list = [item]
        for index_value in range(0, len(self.list)):
            new_list.append(self.list[index_value])
        
        self.list = new_list

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # TODO: Return front item, if any
        if self.is_empty():
            return None
        return self.list[-1]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return front item, if any
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        return self.list.pop(-1)






# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
# Queue = LinkedQueue
Queue = ArrayQueue
