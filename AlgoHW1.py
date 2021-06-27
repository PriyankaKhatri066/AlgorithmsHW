# Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

# O(n)
num = int(input('Enter a number: '))
def sumOfAllnDigits(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum
print(sumOfAllnDigits(num))

# O(1)
# def sum2(n):
#     return (n *(n+1))/2
# print(sum2(num))


# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

# O(1)
num1 = int(input('Enter First number: '))
num2 = int(input('Enter Second number: '))
num3 = int(input('Enter Third number: '))
def max_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n3 and n2 > n1:
        return n2
    return n3
print(max_number(num1, num2, num3))

# def max2(a,b,c):
#     return max(a,b,c)
# print(max2(num1,num2,num3))



# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

num4 = int(input('Enter more than 5 digit number: '))
def odd_even_count(n):
    odd_count = 0
    even_count = 0
    for last_digit in str(n):
        last_digit = int(last_digit)
    # while n != 0:
    #     last_digit = n % 10
        if last_digit % 2 == 0:
            odd_count += 1
        else:
            even_count += 1
        n = n // 10
    return ['Even: ' + str(even_count), 'Odd: ' + str(odd_count)]
print(odd_even_count(num4))




