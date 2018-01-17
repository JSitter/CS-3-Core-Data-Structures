#!python
from recursion import factorial

def combination(n, k):
    top = factorial(n)
    bottom = factorial( n - k ) * factorial(k)

    return top / bottom

if __name__ == "__main__":
    print(combination(52, 5))