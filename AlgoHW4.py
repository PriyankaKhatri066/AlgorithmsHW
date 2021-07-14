# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

def arith_mean(ary):
    sum = 0
    mean = 0
    lower = []
    for i in range(0, len(ary)):
        sum += ary[i]
    mean = sum / len(ary)
    for i in range(0, len(ary)):
        if ary[i] < mean:
           lower.append(ary[i])
    return (sum, mean, lower)
print(arith_mean([1, 3, 5, 6, 4, 10, 2, 3]))



# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
def two_lowest_elements(ary):
    lowest1 = lowest2 = ary[0]
    for i in range(0, len(ary)):
        if ary[i] < lowest1:
            lowest2 = lowest1
            lowest1 = ary[i]
        elif (ary[i] < lowest2 and ary[i] == lowest1):
            lowest2 = ary[i]
    return (lowest1, lowest2)
print(two_lowest_elements([198, 3, 4, 9, 10, 9, 2]))
