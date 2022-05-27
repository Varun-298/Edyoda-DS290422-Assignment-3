# Game of "Functions"
# Write a Python function to sum all the numbers in a list.

data = []

def summation(list_size):

    sum = 0

    for i in range(size):

        val = int(input('Please provide the value:'))
        
        data.append(val)
        
        sum += val
    
    return sum

size = int(input("please provide the size of list:"))

result = summation(size)

data = tuple(data)

print("Your provided input:",data)

print('Sum of your provided inputs:',result)
