#!python
from recursion import factorial

def combination(n, k):
    #Naive Solution
    numerator = factorial(n)
    denominator = factorial( n - k ) * factorial(k)

    return numerator / denominator

def permutation_generator():
    ''' return all permutations of given list in list of lists '''

if __name__ == "__main__":
    print(combination(52, 5))