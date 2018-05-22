# After calling the function findSum() with any number of non-negative integer arguments, 
# it should return the sum of all those arguments. If no arguments are given, 
# the function should return 0, if negative arguments are given, it should return -1.

# eg

# find_sum(1,2,3,4); # returns 10 
# find_sum(1,-2);    # returns -1 
# find_sum();        # returns 0

def find_sum(*args):
    if args is None:
        return 0
    for i in args:
        if(i<0):
            return -1
    return sum(args)
    
# Another shorter solution can be

def find_sum(*args):
    return -1 if any(x < 0 for x in args) else sum(args)
