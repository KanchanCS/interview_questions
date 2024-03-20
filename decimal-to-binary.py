#Decimal to Binary & vice versa

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'
    binary_num = ''
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
    return binary_num

# Example usage:
decimal_num = 10
binary_num = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is: {binary_num}")
