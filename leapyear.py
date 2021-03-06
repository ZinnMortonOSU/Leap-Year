def leapyear(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            return "is not a leap year"
        else:
            return "is a leap year"
    else:
        return "is not a leap year"