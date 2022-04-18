# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Iterative Sort - O(n^2)
#
# NAME:         Michael Usher
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write an O(n^2) sort function `iterative_sort` that
# takes an unordered array of numbers as a parameter
# and returns a sorted array using bubble sort, insertion
# sort, or selection sort using loops, rather than recursion.

def iterative_sort(array):
    # length of the array
    n = len(array)
    # iterate over the array
    for i in range(n):
        for j in range(0, n - i - 1):
            # compare elements and swap of needed
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    # returns the sorted array
    return array

def main():
    print("Sorted: ", [i for i in range(-45,5, 2)] + [i for i in range(100,-34, -15)] + [i for i in range(1000,340, -47)])
main()
