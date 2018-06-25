# You start with a value in dollar form, e.g. $5.00. You must convert this value to a string in which the value is said, 
# like '5 dollars' for example. This should account for ones, cents, zeroes, and negative values. Here are some examples:

# dollar_to_speech('$0.00') == '0 dollars.'
# dollar_to_speech('$1.00') == '1 dollar.'
# dollar_to_speech('$0.01') == '1 cent.'
# dollar_to_speech('$5.00') == '5 dollars.'
# dollar_to_speech('$20.18') == '20 dollars and 18 cents.'
# dollar_to_speech('$-1.00') == 'No negative numbers are allowed!'
# These examples account for pretty much everything. This kata has many specific outputs, so good luck!

def convert(value):
  if "-" in value:
    return "It can not be a negative value!"
  d, c = (int(n) for n in value.replace("$", "").split("."))
  dollars = "{} dollar{}".format(str(d), "s" if d != 1 else "") if d or not c else ""
  link = " and " if d and c else ""
  cents = "{} cent{}".format(str(c), "s" if c != 1 else "") if c else ""
  return "{}{}{}.".format(dollars, link, cents)
  
