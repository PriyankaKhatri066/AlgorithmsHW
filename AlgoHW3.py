# Reverse a Statement
# Build an algorithm that will print the given statement in reverse.
# Example: Initial string = Everything is hard before it is easy
# Reversed string = easy is it before hard is Everything

str1 = 'Everything is hard before it is easy'
str1_list = str1.split()
print(str1_list)
rev_list = str1_list[::-1]
print(rev_list)
rev_str1 = ' '.join(rev_list)
print(rev_str1)



# Permutations
# Write a solution that will print all permutations of a string.
# A permutation is an act of changing the arrangement of characters.
# Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

from itertools import permutations
def permutation(str2):
    perm = [''.join(p) for p in permutations(str2)]
    return perm
print(permutation('ABC'))



# Count Characters
# Create a program that will count vowels and consonants in a string.
# Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}

def count_char(str):
    vowels = 0
    consonants = 0
    for c in str:
        if c == ' ':
            continue
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
            vowels += 1
        else:
            consonants += 1
    return f'vowels = {vowels} and consonants = {consonants}'
print(count_char("hello World"))
