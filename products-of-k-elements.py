# Given a list of numbers and a positive integer k, find the minimum and maximum possible product of k elements taken from the list.

# If you cannot take enough elements from the list, return None/nil

import itertools

def find_min_max_product(arr, k):
    if k > len(arr):
        return None
    products = []
    comb = itertools.combinations(arr,k)
    for i in comb:
        product = 1
        for x in i:
            product *= x
        products.append(product)
    return (min(products), max(products))
    
# Another solution can be

from functools import reduce
from itertools import combinations
from operator import mul

def find_min_max_product(arr, k):
    if k <= len(arr):
        prods = [ reduce(mul, nums) for nums in combinations(arr, k) ]
        return min(prods), max(prods)
