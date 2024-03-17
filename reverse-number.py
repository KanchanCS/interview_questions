#Reverse a Number.
def is_reverse(num_list):
    length = len(num_list)
    for i in range(length//2):
        num_list[i], num_list[length-i -1] = num_list[length -i -1],  num_list[i]
        return num_list

#Main function to call the above function and
#print the reversed number
num_list=[1,5, 9, 8,3]
print(is_reverse(num_list))