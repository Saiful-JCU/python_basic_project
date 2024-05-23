'''# max of two

a = 4
b = 9
if a > b:
    print(a)
else:
    print(b)

num1 = int(input("first number: "))
num2 = int(input("second number: "))
if (num2 >= num1):
    largest = num2
else:
    largest = num1
print("Largest number you entered is: ", largest)

num3 = int(input("first number: "))
num4 = int(input("second number: "))
maximum = max(num3, num4)
print("maximum number is: ", maximum)'''

# Max of three
'''a = 8
b = 34
c = 949
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("max of three: ", largest)

d =30
e =34
f = 324
max_of_three = max(d, e, f)
print("max number: ", max_of_three)'''

# average of numbers

element = int(input("how many element you want to enter: "))

total = []
for i in range(element):
    num = float(input("Enter your number one by one: "))
    total.append(num)
sum = sum(total)
avarage = sum / element
print(avarage)

len = int(input("how many element you have: "))
num = 0
for x in range(0, len):
    element = float(input(f"enter your number {x+1}: "))
    num += element
avarage2 = num / len
print(avarage2)