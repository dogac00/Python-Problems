# Task
# Given an array/list [] of integers , Find the product of the k maximal numbers.

# Notes
# Array/list size is at least 3 .

# Array/list's numbers Will be mixture of positives , negatives and zeros

# Repeatition of numbers in the array/list could occur.

# Input >> Output Examples
# maxProduct ({4, 3, 5}, 2) ==>  return (20)

from functools import reduce
from operator import mul

def max_product(lst, n_largest_elements):
    return reduce(mul,sorted(lst)[-n_largest_elements:])
    
# Or with another way

def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    prod = 1
    for i in lst[n_largest_elements:]:
        prod *= i
    return prod
    
# Or...

from functools import reduce
from operator import mul
from heapq import nlargest

def maxProduct (lst, n):
    return reduce(mul, nlargest(n, lst))
