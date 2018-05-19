# Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.

# Given a number, Find if it is Disarium or not.

def disarium_number(number):
    dis_num = 0
    position = 1
    for i in str(number):
        dis_num += int(i) ** position
        position += 1
    return dis_num == number
