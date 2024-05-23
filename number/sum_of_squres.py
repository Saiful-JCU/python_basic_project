'''
take a number as a input. then get the sum of the numbers. if the number is n. then get
0*2 + 1*2 + 2*2 + 3*2 +..........+ n*2
'''

def square_number(num):
    sum = 0
    for i in range(num + 1):
        square =i ** 2
        sum  = sum + square
    return sum
num = int(input("enter a number: "))
square_result = square_number(num)
print("sum of square from your number is: ", square_result)


multi = 3 ** 2
print(multi)