'''
find the largest of the three numbers.
'''
# user_input = input("enter multiple values separated by a comma: ")
#
# # split the input string based on the comma delimiter
# values = user_input.split(',')
#
# # convert the values to integers (or floats if needed)
# values = [float(val.strip()) for val in values]
#
# print("values entered by the user: " , values)

'''
solution with simple if - else 
'''

num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))
# largest =  num1

# if (num2 >= num1) and (num2 >=3):
#     largest = num2
# elif (num3 >= num2) and (num3 >= num1):
#     largest = num3
# else:
#     largest = num1
# print("largest number you entered is: ", largest)

'''shortcut'''
largest1 = max(num1, num2, num3)
print("largest number you entered is: ", largest1)


'''
in summary you have use max() function to get the largest number to easiest way.
'''

