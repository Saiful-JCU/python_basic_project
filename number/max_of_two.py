'''
find the largest of two numbers..
'''

def max_of_two(num1, num2):
    thislist = []
    thislist.append(num1)
    thislist.append(num2)
    largerst = max(thislist)
    return largerst
# num1 = float(input("write any number: "))
# num2 = float(input("write any number: "))

max1 = max_of_two(10, 30)
print(max1)


# we have another way to solve this problem
print("2nd way to solve this problem.")
# number1 = float(input("write your first number: "))
# number2 = float(input("write your second number: "))
# if (number1 >= number2):
#     largest = number1
# else:
#     largest = number2
# print("largest number you entered is:  ", largest)


# shorthand
'''
this simple and alternative solution is to send the numbers to the max function.
'''
# numbers = float(input("First Number: "))
# numbers0 = float(input("Second Number: "))
# maximum = max(numbers, numbers0)
# print("max of two numbers you entered is: ", maximum)

'''alternative solution '''
num3 = float(input("your first number: "))
num4 = float(input("your second number: "))
if (num3 - num4 > 0 ):
    print("the bigger number is: ", num3)
else:
    print("the bigger number is: ", num4)
    