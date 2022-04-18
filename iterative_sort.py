# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: Iterative Sort - O(n^2)
#
# NAME:         FIXME
# ASSIGNMENT:   Project 4: Sorting & Searching

# Write an O(n^2) sort function `iterative_sort` that
# takes an unordered array of numbers as a parameter
# and returns a sorted array using bubble sort, insertion
# sort, or selection sort using loops, rather than recursion.
def iterative_sort(array):
    return array

def main():
    arrays = [ [45, 67, -2, 33, 0, -44, 134, -67], \
               [i for i in range(10)], \
               [i for i in range(10,-1, -1)] ]

    for a in arrays:
        print("Unordered:", a)
        print("Sorted:   ", iterative_sort(a))

main()
