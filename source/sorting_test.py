#!python

from sorting import (is_sorted, bubble_sort, selection_sort, insertion_sort,
                     merge_sort, random_ints, merge, split_sort_merge)
import unittest


# Change this variable to the sort function you want to test
sort = insertion_sort


class IsSortedTest(unittest.TestCase):

    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        # Write more positive test cases with assert is True statements
        assert is_sorted([0, 1, 10, 100])
        assert is_sorted([-2, -1, 0])
        assert is_sorted([1234, 12345, 123456])

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        # Write more negative test cases with assert is False statements
        assert is_sorted([5577, 577, 77 ]) is False
        assert is_sorted([0, 1, 2, 3, 0]) is False
        assert is_sorted([22, 222, 2222, 2]) is False

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        #Wrote More tests
        assert is_sorted(["B", "C", "A"]) is False
        assert is_sorted(["B", "c", "A"]) is False
        assert is_sorted(["r", "S", "T", "r", "S", "T"]) is False
        assert is_sorted(["98", "A", "a", "b"]) is True

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        # Write more negative test cases with assert is False statements
        assert is_sorted(['Stringy', "String", "Strin"]) is False
        assert is_sorted(['Pinapples', "'"]) is False

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
        #Write more positive test cases with assert is True statements
        assert is_sorted([(3, 3), (3, 4), (4, 3)]) is True
        assert is_sorted([ ( "ABA", 3 ), ("ABB", 3), ("ABB", 3) ]) is True

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        # Write more negative test cases with assert is False statements
        assert is_sorted([ (3, 3), (4, 3),  (3, 3)]) is False
        assert is_sorted([ ("The", "CAT"), ("Is", 3), ("Carosel", 0) ]) is False


class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        # Write more test cases with assert equal list statements
        # You'll need a lot more than this to test sorting algorithm robustness

        items5 = [0, 1, 2, 3]
        sort(items5)
        assert items5 == [0,1,2,3]
        items6 = [4333, 3433, 3343, 3334]
        sort(items6)
        assert items6 == [3334, 3343, 3433, 4333]

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        # Create lists of integers with many duplicate values
        # Write more test cases with assert equal list statements
        items5 = [89, 89, 89, 9]
        sort(items5)
        assert items5 == [ 9, 89, 89, 89]
        items6 = [78, 45, 23, 78, 45, 23]
        sort(items6) 
        assert items6 == [23, 23, 45, 45, 78, 78]
        

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        # Write more test cases with assert equal list statements
        # You'll need a lot more than this to test sorting algorithm robustness
        items4 = ['T', 'B', 'C', 'A']
        sort(items4)
        assert items4 == ["A", "B", "C", "T"]
        items5 = [ "Ruff", "1", "98", "'"]
        sort(items5)
        assert items5 == [ "'", "1", "98", "Ruff"]

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        sort(items)  # Call mutative sort function to sort list items in place
        assert items == sorted_items

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items

class MergeTest(unittest.TestCase):
    def test_merge(self):
        items1 = ["Bananas", "Picadilly", "Picasso"]
        items2 = ["August", "Picadilly", "Rearing"]
        new_list = merge(items1, items2)
        print(new_list)
        assert new_list == ["August", "Bananas", "Picadilly", "Picadilly", "Picasso", "Rearing"]

class MergeSort(unittest.TestCase):
    def test_merge_sort(self):
        unsorted_list = ["Potatoes", "Transfat", "Toes", "Squealed", "Impossibru", "Bastion"]
        sorted_list = ["Bastion", "Impossibru","Potatoes","Squealed","Toes","Transfat"] 
        assert split_sort_merge(unsorted_list) == sorted_list 

if __name__ == '__main__':
    unittest.main()
