#Decimal to Octal.

# without function
# Taking decimal number as input
# decimal_number = int(input("Enter a decimal number: "))

# # Converting decimal to octal using oct() function
# octal_number = oct(decimal_number)

# print("The octal equivalent of", decimal_number, "is", octal_number)



#Converting a decimal number to octal involves repeatedly dividing the decimal number by 8 
# and recording the remainders. The remainders, obtained from each division operation, 
# are then arranged in reverse order to obtain the octal representation of the decimal number.

#Here's a Python program to perform this conversion:

def decimal_to_octal(decimal):
    octal_digits = []

    # Handle the case when the decimal number is 0
    if decimal == 0:
        octal_digits.append(0)

    # Convert decimal to octal
    while decimal > 0:
        remainder = decimal % 8
        octal_digits.append(remainder)
        decimal //= 8

    # Reverse the list of octal digits obtained
    octal_digits.reverse()

    # Convert the list of octal digits to a string
    octal_string = ''.join(map(str, octal_digits))

    return octal_string

# Test the function
decimal_number = int(input("Enter a decimal number: "))
octal_number = decimal_to_octal(decimal_number)
print("The octal equivalent of", decimal_number, "is", octal_number)
