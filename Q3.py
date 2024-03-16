def is_leap_year(year):
    # Leap years are divisible by 4
    if year % 4 == 0:
        # Except for years that are divisible by 100
        # But leap years divisible by 400 are still leap years
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
