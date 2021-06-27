# Split in Half.
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

str1 = 'CareeristAutomation'
def swap_halves(str):
    first_half = []
    second_half = []
    if len(str) % 2 == 0:
        first_half = str[0:len(str)//2]
        second_half = str[len(str)//2:]
    else:
        first_half = str[0:(len(str)//2)+1]
        second_half = str[-(len(str)//2):]
    return (second_half + first_half)
print(swap_halves(str1))



# Unique Characters in String.
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.


str2 = input('Enter a string: ')
def unique_char(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return False
    return True
print(unique_char(str2))

