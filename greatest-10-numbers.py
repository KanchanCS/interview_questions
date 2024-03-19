#Greatest among 10 numbers.

def mymax(list1):
    max = list1[0]
    for i in list1:
        if  i > max:
            max = i
    return max
list1 = [1,2,3,4]
print(mymax(list1))    


 