# Question 2: Count Vowels in a String Write a Python function to count the number of vowels in a given string.
# Consider both uppercase and lowercase vowels.

# Example:

# Input: "Hello World"
# Output: 3


def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    count = sum(s.count(vowel) for vowel in vowels)
    return count


input_string = "Hello World"
print("Input:", input_string)
print("Output:", count_vowels(input_string))
