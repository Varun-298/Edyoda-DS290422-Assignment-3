# Calculate the Upper and The lower Case
# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def case_count(name):

    ucount=0
    
    for i in name:
        a = i.isupper()
        if a == True:
            ucount +=1
    return ucount

name = input('Please Enter a name : ')
a = list(name)
b = len(name)-1

upperc = case_count(name)
lowerc = b-upperc+1

print("No. of Upper case characters within your provided name",name,"is",upperc)
print("No. of Lower case characters within your provided name",name,"is",lowerc)
