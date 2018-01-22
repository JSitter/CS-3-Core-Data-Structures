#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.list.size == 0:
            return True
        else:
            return False


    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack.
        """
        # TODO: Push given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.list.tail:
            return self.list.tail.data
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O TODO"""
        # TODO: Remove and return top item, if any
        if self.list.size <= 0:
            raise ValueError("Stack is empty")

        item_index = self.list.size - 1

        cur_node = self.list.head

        cur_index = 0
        if self.list.size > 2:
            for _ in range(0, item_index - 1):
                cur_node = cur_node.next
                cur_index = _
            
            node_before = cur_node
            self.list.tail = node_before
            return_value = node_before.next.data
            node_before.next = None

        elif self.list.size == 2:
            return_value = cur_node.next.data
            cur_node.next = None
            self.list.tail = cur_node

        else:
            #only one item left in stack
            return_value = cur_node.data
            self.list.head = None
            self.list.tail = None

        self.list.size -= 1
        return return_value



# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O  Why TODO"""
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – Why [Must iterate]"""
        # TODO: Remove and return top item, if any
        if len(self.list) == 0:
            raise ValueError("Stack is empty")
        item = self.list[-1]
        if len(self.list) > 1:
            self.list = self.list[0:-1]
        else:
            self.list = list()
        
        return item


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
