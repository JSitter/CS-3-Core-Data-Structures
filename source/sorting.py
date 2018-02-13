#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions? Under most conditions and worst case.
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(items) <= 1:
        return True
    
    first_index = 0
    second_index = 1

    while items[first_index] <= items[second_index]:
        if second_index <= len(items) - 2:
            second_index += 1
            first_index += 1
        else:
            return True
    
    return False

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    
    sort_list = items

    if len(sort_list) <= 1:
        return sort_list
    first_index = 0
    second_index = 1
    in_sorted_order = False

    while not in_sorted_order:
        if sort_list[first_index] <= sort_list[second_index]:
            if second_index <= len(sort_list) - 2:
                second_index += 1
                first_index += 1
            else:
                return sort_list
        else:
            #swap!
            first_item = sort_list[first_index]
            sort_list[first_index] = sort_list[second_index]
            sort_list[second_index] = first_item
            first_index = 0
            second_index = 1




def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    sort_array = items
    #Repeat until all items are in sorted order
    for min_index in range(0,len(items)):
    # Find minimum item in unsorted items

        unsorted_index = min_index + 1
        while unsorted_index < len(items):

            if sort_array[unsorted_index] < sort_array[min_index]:
                #Swap it with first unsorted sort_array
                unsorted_item = sort_array[min_index]
                sort_array[min_index] = sort_array[unsorted_index]
                sort_array[unsorted_index] = unsorted_item

            unsorted_index += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted items, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    
    # Repeat until all items are in sorted order
    for unsorted_index in range(1, len(items)):
        sort_item = items[unsorted_index]
        search_index = unsorted_index - 1
        insert_index = unsorted_index
        while search_index >= 0:
            if items[search_index] < sort_item:
                items[insert_index] = sort_item
            else:
                items[insert_index] = items[search_index]
                search_index -= 1
        



    # : Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    list1_index = 0
    list2_index = 0
    new_list = list()

    # Repeat until one list is empty
    while len(items1) > list1_index and len(items2) > list2_index:
        # Find minimum item in both lists and append it to new list
        if items1[list1_index] <= items2[list2_index]:
            new_list.append(items1[list1_index])
            list1_index += 1
        else:
            new_list.append(items2[list2_index])
            list2_index += 1
    # Append remaining items in non-empty list to new list
    if list1_index < len(items1):
        while list1_index < len(items1):
            new_list.append(items1[list1_index])
            list1_index += 1
    elif list2_index < len(items2):
        while list2_index < len(items2):
            new_list.append(items2[list2_index])
            list2_index += 1

    return new_list





def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    list1 = list()
    list2 = list()
    iterator_index = 0

    # Split items list into approximately equal halves
    while iterator_index < len(items):
        if iterator_index % 2 == 0:
            list1.append(items[iterator_index])
        else:
            list2.append(items[iterator_index])
        iterator_index += 1

    # Sort each half using any other sorting algorithm
    selection_sort(list1)
    selection_sort(list2)
    # Merge sorted halves into one list in sorted order
    return merge(list1, list2)

    
    


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=selection_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    #Test Merge function
    items1 = ["Bananas", "Picadilly", "Picasso"]
    items2 = ["August", "Picadilly", "Reaming"]
    new_list = merge(items1, items2)
    print(new_list)

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)



if __name__ == '__main__':
    main()
