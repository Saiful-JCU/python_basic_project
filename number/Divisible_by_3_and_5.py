'''
for a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5

'''

def divisible_number(num):
    result = []
    for i in range(num):
        if i % 3 ==0 and i %5 ==5:
            result.append(i)
            return result

num = int(input("give any integer number: "))
result =divisible_number(num)
print(result)

# another way to solve this problem without using function, but while loop

num = int(input('insert a number: '))

result = []
i = 1
while i <= num:
    if i % 3 == 0 and i % 5 == 0:
        result.append(i)
    i = i+1

print(result)