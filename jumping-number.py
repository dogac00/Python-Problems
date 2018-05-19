# Jumping number is the number that All adjacent digits in it differ by 1.

# Given a number, Find if it is jumping or not.

def jumping_number(number):
    str_num = str(number)
    length = len(str_num)
    
    if(length == 1):
        return "Jumping!!"
    
    for i in range(1, length):
        if(abs(int(str_num[i-1]) - int(str_num[i])) != 1):
            return "Not!!"
    return "Jumping!!"
