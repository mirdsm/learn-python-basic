
input_number = int(raw_input('Input Your Number! \n>'))
def number_to_str(i):
    try:
        number_str = str(i)
        strng = list(number_str)
        number_2nd = strng[1]
    except IndexError:
        return i
    else:
        return number_2nd

def number_to_str2(i):
    try:
        number_str = str(i)
        strng = list(number_str)
        number_3th = strng[0]
    except IndexError:
        return i
    else:
        return number_3th

def number_to_str3(i):
    try:
        number_str = str(i)
        strng = list(number_str)
        number_4th = strng[2]
    except IndexError:
        return i
    else:
        return number_4th

for i in range(0, (input_number + 1)):
    if i == 4:
        print "NUMBER FOUR HAS BEEN BLOCKED!"
    elif number_to_str(i) == "4":
        print "NUMBER FOUR HAS BEEN BLOCKED!"
    elif number_to_str2(i) == "4":
        print "NUMBER FOUR HAS BEEN BLOCKED!"
    elif number_to_str3(i) == "4":
        print "NUMBER FOUR HAS BEEN BLOCKED!"
    else:
        print i
