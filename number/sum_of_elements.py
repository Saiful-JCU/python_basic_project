'''
for a given list, get the sum of each number in the list.
'''

def sum_of_elements(list):
    sum = 0
    for num in list:
        sum = sum + num
    return sum

list = [13,312,42,424,5,4,46]

total = sum_of_elements(list)
print("the total sum of given number is: ", total)

# solution without function

nums = [13,312,42,424,5,4,46]
total = sum(nums)
print(total)