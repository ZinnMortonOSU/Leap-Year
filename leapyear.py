def leapyear(year):
    if(year % 4 == 0):
        if(year % 100 == 0):
            if(year % 400 == 0):
                return "is a leap year"
            else:
                return "is not a leap year"
        else:
            return "is a leap year"
    else:
        return "is not a leap year"

inputYearStr = input("Input a year: ")

if(inputYearStr.isnumeric()):
    inputYear = int(inputYearStr)

    print(inputYearStr + " " + leapyear(inputYear))
else:
    print("Please enter a positive integer")