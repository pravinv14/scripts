'''
User will require to input a year to find if it is a leap year or not
'''
def is_leap(year):
    leap = False
    
    if (year % 4) == 0:
        if (year % 100) != 0:
            return True
        elif (year % 400) == 0:
            return True
    return leap

year = int(input("Enter a year : "))
