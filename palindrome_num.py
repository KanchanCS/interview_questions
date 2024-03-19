#Palindrome program
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same 
# forward and backward, ignoring spaces, punctuation, and capitalization.
# Examples of palindromic words:
# "radar"
# "level"
# "deified"
# "civic"

# Slution==1
# def is_pai(num):
#     return num == num[::-1]
# num = int(input("Enter a number: "))
# ans = is_pai(num)
# if  ans:
#     print("yes")
# else:
#     print("no")  

# Slution==2
def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

word = input("Enter a word:")
if is_palindrome(word):
    print("palindrome")
else:
    print("not paildrome")    
    
    
    
    
    


