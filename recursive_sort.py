# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: Recursive Sort < O(n^2)
#
# NAME:         FIXME
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a less than O(n^2) sort function `recursive_sort`
# that takes an unordered array of numbers as a parameter
# and returns a sorted array using merge sort or quick
# sort using recursion, rather than loops.

def recursive_sort(array):
    if array == []:
        return []
    pivot = array[0] # array gets sorted
    p = [e for e in array if e == pivot]
    smaller = recursive_sort([e for e in array if e < pivot])
    greater = recursive_sort([e for e in array if e > pivot])
    return smaller + p + greater # returns the values from smaller to greatest

def main():
    # all of the arrays from the test case
    arrays = [[45, 67, -2, 33, 0, -44, 134, -67],
              [i for i in range(10)],
              [i for i in range(10, -1, -1)],
              [i for i in range(-10,-1, 1)] + [i for i in range(10,-1, -1)],
              [i for i in range(-45,5, 2)] + [i for i in range(100,-34, -15)] + [i for i in range(1000,340, -47)]]

    for a in arrays: # loop to test all of the cases
        print("Unordered:", a)
        print("Sorted:    ", recursive_sort(a))

main()
