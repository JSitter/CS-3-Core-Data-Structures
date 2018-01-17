#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    
    # Just do it Python
    # text = sanitizeText(text)
    # if text[::-1] == text:
    #     return True
    # else:
    #     return False

    # Specifically iterative python
    clean_text = sanitizeText(text)
    for x in range(0, len(clean_text) - 1):
        if clean_text[x] != clean_text[-1 - x]:
            return False
    return True



def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    text = sanitizeText(text)

    text_len = len(text)
    if left == right:

        if left == None and text_len <= 1:
            return True
 
        #if left and right are same then middle doesn't matter
        if text_len <2 and left is not None:
            return True
        else:
            new_text = text[1:-1]
            return is_palindrome_recursive(new_text, text[0], text[-1])
    else:
        return False


def sanitizeText(sourceText):
    '''
        Santize words
    '''
    acceptedChars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return ''.join(filter(acceptedChars.__contains__, sourceText)).lower()

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    #main()
    if is_palindrome("ABCZBA"):        
        print("Checkly Weckle")
