# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n) between 0 and n. 
# Count the numbers of digits d used in the writing of all the k**2. 
# Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count. 

def nb_dig(n, d):
    squares = map(str, [i*i for i in range(0,n+1)])
    count = 0
    for square in squares:
        count += square.count(str(d))
    return count
    
# Another solution which is a one-liner is:

def nb_dig(n, d):
    return sum(str(i*i).count(str(d)) for i in range(n+1))
