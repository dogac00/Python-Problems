# Write a function that takes an integer and returns an array [A, B, C], where A is the number of multiples of 3 (but not 5) 
# below the given integer, B is the number of multiples of 5 (but not 3) below the given integer and C is the number of 
# multiples of 3 and 5 below the given integer.

# For example, solution(20) should return [5, 2, 1]

def solution(number):
    a,b,c = 0,0,0
    for i in range(3, number):
        if i % 15 == 0:
            c += 1
        elif i % 5 == 0:
            b+= 1
        elif i % 3 == 0:
            a += 1
    return [a,b,c]
    
# Anohter shorter and faster solution is

def solution(number):
    A = (number - 1) // 3
    B = (number - 1) // 5
    C = (number - 1) // 15    
    return [A - C, B - C, C]
