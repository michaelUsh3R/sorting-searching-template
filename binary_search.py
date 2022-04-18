# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: Recursive Binary Search
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write a recursive function `search` that
# takes an ordered array of numbers as a parameter
# and a number to search for and returns the index
# of the number in the array using binary, or -1 otherwise. For
# full credit, the search should be implemented using
# recursion, rather than a loop.
def binary_search(array, num):
    return search(array, num, 0, len(array) - 1)

def search(array, num, min, max): # searches throughout the whole list
    if min > max:
        return -1
    else:
        mid = (min + max) // 2
    if array[mid] == num:
        if mid != (len(array)-1):
            if array[mid+1] == array[mid]:
                return mid - 1
            else:
                return mid
        else:
            return mid
    elif array[mid] > num:
        return search(array, num, min, mid - 1)
    else:
        return search(array, num, mid + 1, max)

def main():
    a = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3] # test case
    index = binary_search(a, 1)
    print("Element found at index: ", index) #outputs the index of the element found in the array

main()
