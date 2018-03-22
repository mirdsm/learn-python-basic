



def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
''''
def is_leap(year):
    leap = False
    if 1900 >= year >= 10**5:
        return leap
    else:
        y = year
        x = year % 400
        if x == 0:
            leap = True
            return leap
        else:
            y = y % 4
            if y == 0:
                leap = True
                return leap
            else:
                return leap

def is_leap(year):
    leap = False
    if 1900 >= year >= 10**5:
        y = year
        x = year % 400
        if x == 0:
            leap = True
            return leap
        else:
            y = y % 4
            if y == 0:
                leap = True
                return leap
            else:
                return leap

    else:
        return leap
'''
year = int(raw_input())
print is_leap(year)
