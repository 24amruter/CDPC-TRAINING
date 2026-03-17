#1. compare triplet
def compareTriplets(a, b):
    alice = 0
    bob = 0
    i = 0
    while i < len(a):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
        i += 1
    return (alice, bob)


#2. sum big
def compareTriplets2(a, b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    return alice, bob


#3. sum of diagonal of matrix
def diagonalDifference(arr):
    sum1 = 0
    sum2 = 0
    n = len(arr)
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][n - i - 1]
    return abs(sum1 - sum2)


#4. plus minus
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1
    n = len(arr)
    print(pos / n)
    print(neg / n)
    print(zero / n)


#5. Shifting array by n steps
n = int(input("Enter the number of Elements: "))
arr = []
for i in range(n):
    a = int(input("Enter the number: "))
    arr.append(a)

b = int(input("Enter the number of steps: "))
b = b % n
arr = arr[-b:] + arr[:-b]

for i in range(n):
    print(arr[i])