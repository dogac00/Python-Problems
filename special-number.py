# A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5.

# Given a number determine if it special number or not.

special = set("012345")

def special_number(number):
    return "Special!!" if set(str(number)) <= special else "NOT!!"
