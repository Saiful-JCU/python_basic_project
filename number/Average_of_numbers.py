'''
take numbers from a user and show the average ot the numbers the user entered.
Hint
To solve this problem.
First, ask the user - how many numbers you want to enter? then, run a for-loop. each time, take input from
the user and put it in a list.
Once you get all the numbers, you can send the list to the sum function. the sum function will add all the numbers and
give you the total.
Finally, divide the total by the number of elements the user entered.
'''

n = int(input("How many numbers you want to enter?: "))
total = []

for i in range(n):
    numbers = float(input(f"Enter element {i+1}: "))
    total.append(numbers)
nums = sum(total)
average = nums / n
print(average)
