# Create the hi_all() function without using strings, numbers and booleans. 
# The return value is "Hello World". No, it is not impossible, use the builtin functions. Good luck :)

def hi_all():
  one =  -~len([])
  two = one + one
  three = one + two
  four = two * two
  five = three + two
  seven = four + three
  eight = four * two
  ten = pow(three, two) + one
  hundred = ten * ten;

  H = chr((seven * ten) + two)
  e = chr(hundred + one)
  l = chr(hundred + eight)
  o = chr(hundred + ten + one)
  sp= chr(eight * four)
  W = chr((eight * ten) + seven)
  r = chr(hundred + ten + four)
  d = chr(hundred)
  
  return H+e+l+l+o +sp+ W+o+r+l+d
  
# Another solution can be
  
one = len([[]])
two = len([[],[]])
three = len([[],[],[]])
five = len([[],[],[],[],[]])
def Hello_World():
    pass
def hi_all():
    return str(Hello_World)[five*two:five*three] + str(Hello_World)[three*(five+two)] + str(Hello_World)[two**(two*two):three*(five+two)]
