# def concatenate_strings_with_join(string1, string2):
#     concatenated_string = ''.join([string1, string2])
#     return concatenated_string

# # Testing the function with two strings
# str1 = "Hello "
# str2 = "World"
# result = concatenate_strings_with_join(str1, str2)
# print("Concatenated string:", result)


def concatenate_strings(string1, string2):
    concatenated_string = string1 + string2
    return concatenated_string

# Example usage:
str1 = "Hello "
str2 = "World"
result = concatenate_strings(str1, str2)
print("Concatenated string:", result)
