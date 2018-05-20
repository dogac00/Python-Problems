# Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, 
# only prime numbers are multiplied to calculate the primorial of a number. 
# It's denoted with P#.

# Task
# Given a number N , calculate its primorial.

def is_prime(n):
  if n == 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

def num_primorial(n):
    primorial = 1
    count = 0
    num = 2
    while(1):
        if count == n:
            break
        elif is_prime(num):
            primorial *= num
            num += 1
            count += 1
        else:
            num += 1
    return primorial
