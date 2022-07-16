"""With User Entering Numbers"""


def smallestDiff(list, n):
    list.sort()
    inf = 1000
    for i in range(n - 1):
        if list[i + 1] - list[i] < inf:
            inf = list[i + 1] - list[i]
    return inf


n = int(input("Enter Number of list here "))
list = []
for j in range(n):
    element = int(input('Enter number '))
    list.append(element)

print("Minimum difference is " + str(smallestDiff(list, n)))

"""Without User Entering Numbers"""


def smallestDiff(list, n):
    list.sort()
    inf = 1000
    for i in range(n - 1):
        if list[i + 1] - list[i] < inf:
            inf = list[i + 1] - list[i]
    return inf


list = [1, 5, 3, 19, 18, 25]
n = len(list)
print("Minimum difference is " + str(smallestDiff(list, n)))
