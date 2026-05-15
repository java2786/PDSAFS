# Check whether the input year is a leap year using logical operators.

year = 1900

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")
