def is_leap_year(year):
    # Leap years are divisible by 4
    if year % 4 == 0:
        return f"{year} is a leap year"
    else:
        return f"{year}  not is a leap year"

# Test the function
year = int(input("Enter a year: "))
print(is_leap_year(year))

