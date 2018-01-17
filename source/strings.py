#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    #O(n) runtime where n is the number of characters in text string
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    pattern_len = len(pattern)
    text_len = len(text)

    if pattern_len == 0:
        return True

    if text_len < pattern_len:
        return False

    for corpus_index in range(0, text_len):
        matching_index = corpus_index
        pattern_index = 0
        text_char = ""
        pattern_char = ""

        while text_char == pattern_char:
            if text_len - matching_index <= 0:
                return False

            text_char = text[matching_index]
            pattern_char = pattern[pattern_index]

            
            if text_char == pattern_char:
                matching_index += 1
                pattern_index += 1

            if pattern_index >= pattern_len:
                return True
    
    return False

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    #O(n) runtime where n is the length of the text string
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    pattern_len = len(pattern)
    text_len = len(text)

    if pattern_len == 0:
        return 0
    
    if pattern_len > text_len:
        return None

    for corpus_index in range(0, text_len):
        matching_index = corpus_index
        pattern_index = 0
        text_char = ""
        pattern_char = ""

        while text_char == pattern_char:
            if text_len - matching_index <= 0:
                return None

            text_char = text[matching_index]
            pattern_char = pattern[pattern_index]

            
            if text_char == pattern_char:
                matching_index += 1
                pattern_index += 1

            if pattern_index >= pattern_len:
                return corpus_index
    
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    # O(n) for the length of the string carried within the tewxt veriable
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    pattern_len = len(pattern)
    text_len = len(text)
    found_indexes = list()

    if pattern_len == 0:
        for x in range(0, text_len):
            found_indexes.append(x)
        return found_indexes
    
    if pattern_len > text_len:
        return found_indexes

    for corpus_index in range(0, text_len):
        matching_index = corpus_index
        pattern_index = 0
        text_char = ""
        pattern_char = ""

        while text_char == pattern_char:
            if text_len - matching_index <= 0:
                return found_indexes

            text_char = text[matching_index]
            pattern_char = pattern[pattern_index]

            
            if text_char == pattern_char:
                matching_index += 1
                pattern_index += 1

            if pattern_index >= pattern_len:
                found_indexes.append(corpus_index)
                pattern_index = 0
                break
    
    return found_indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
    find_all_indexes('abcabcabc', 'abc')