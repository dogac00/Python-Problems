# Definition
# A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

# Task
# Given a number determine if it Automorphic or not .

def automorphic(n):
    return "Automorphic" if str(n*n)[-(len(str(n))):] == str(n) else "Not!!"
    
# Another solution is

def automorphic(n):
    return "Automorphic" if str(n*n).endswith(str(n)) else "Not!!"

# Or with using modulo

def automorphic(n):
    l = len(str(n))
    return 'Automorphic' if n * n % 10 ** l == n else 'Not!!'
    
