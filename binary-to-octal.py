def binary_to_octal(binary):
    # Ensure that the length of the binary string is a multiple of 3
    while len(binary) % 3 != 0:
        binary = '0' + binary  # Add leading zeros if needed
    
    # Dictionary to map binary triplets to octal digits
    binary_to_octal_dict = {
        '000': '0',
        '001': '1',
        '010': '2',
        '011': '3',
        '100': '4',
        '101': '5',
        '110': '6',
        '111': '7'
    }

    octal = ''
    # Iterate over the binary string in groups of three
    for i in range(0, len(binary), 3):
        # Extract a group of three binary digits
        triplet = binary[i:i+3]
        # Convert the triplet to its octal equivalent and append to the result
        octal += binary_to_octal_dict[triplet]

    return octal

# Test the function
binary_number = input("Enter a binary number: ")
octal_number = binary_to_octal(binary_number)
print("The octal equivalent of", binary_number, "is", octal_number)
