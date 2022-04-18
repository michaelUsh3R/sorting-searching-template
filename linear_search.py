# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: Iterative Linear Search
#
# NAME:         FIXME
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a function `linear_search` that takes an
# unordered array of numbers as a parameter and
# a number to search for and returns the index of
# the number in the array, or -1 otherwise. Your
# search should be performed using a loop, rather
# than recursion.
def linear_Search(list, n, key):
    # Searching list sequentially
    for i in range(0, n):
        if (list[i] == key):
            return i
    return -1

def main():
    list = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3]
    key = 3

    n = len(list)
    res = linear_Search(list, n, key)

    print("Element found at index: ", res)

main()
