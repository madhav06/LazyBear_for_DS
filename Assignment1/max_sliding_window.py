# python 3
# Python3 implementation of the approach

# Function to print the maximum for
# every k size sub-array
def print_max(a, n, k):

    # max_upto array stores the index
    # upto which the maximum element is a[i]
    # i.e. max(a[i], a[i + 1], ... a[max_upto[i]]) = a[i]

    max_upto=[0 for i in range(n)]

    # Update max_upto array similar to
    # finding next greater element
    s=[]
    s.append(0)

    for i in range(1,n):
        while (len(s) > 0 and a[s[-1]] < a[i]):
            max_upto[s[-1]] = i - 1
            del s[-1]

        s.append(i)

    while (len(s) > 0):
        max_upto[s[-1]] = n - 1
        del s[-1]

    j = 0
    for i in range(n - k + 1):

        # j < i is to check whether the
        # jth element is outside the window
        while (j < i or max_upto[j] < i + k - 1):
            j += 1
        print(a[j], end=" ")
    print()

# Driver code

a = [9, 7, 2, 4, 6, 8, 2, 1, 5]
n = len(a)
k = 3
print_max(a, n, k) 
