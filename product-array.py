# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to 
# The Product of all the elements of Arr[] except Arr[i].

def product_array(numbers):
    prod_arr = []
    for i in numbers:
        temp = 1
        for j in numbers:
            temp *= j
        prod_arr.append(temp/i)
    return prod_arr
    
# Another solution using reduce and mul is

from operator import mul
from functools import reduce

def product_array(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]
