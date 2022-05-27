# String inside the function
# Write a Python program to reverse a string.


def reverse_string(val):
    reverse = ""
    for i in range(b,-1,-1):
        reverse = reverse + a[i]
    return reverse

name = input('Please Enter a name : ')
a = list(name)
b = len(name)-1
result = reverse_string(b)

print("The mirror dimension of your enterned name :",name," is:",result)