"""
Stanford - Divide and Conquer Algorithms - Challenge 2
by James Kwon Lee (v2. 6.16.22)

Task: Count Inversions from a list of numbers generated from a .txt file.
- Create a Divide and Conquer Algorithm
- Running time should be approx. O(n) = n log n or faster

Pseudocode for counting Split-Inversions:
- Sort the left and right arrays, then merge into a new array, D.
- While sorting,
    if left array element is larger than right array element,
        the remaining elements of the left array count towards split-inversion count.

v2.0 Updates:
- Removed Python's sort subroutine as sorting is implicit when merge_sort_split_array is called recursively
    - Personal note: I needed to understand recursion and how calls are stacked.
- Refactored count_left and count_right into a single, modular function.
- Placed all recursive calls into a count_inversions function, which allows for the division of arrays at each call.
- Result: Running Time Improved from 3-minutes-30-seconds to <.50-seconds

The Final Answer from 100,000 numbers text file is: 2407905288 Inversions
"""


def main():
    array_a = open("IntegerArray.txt").readlines()
    array_a = list(map(int, array_a))
    result = total_count(array_a)
    print("Inversion Count: ", result)
    return result


def total_count(array):
    return count_inversions(array)[1]


def count_inversions(array):
    # Base Case
    if len(array) <= 1:
        return array, 0

    midpoint = len(array) // 2

    # Recursive Calls to count left, right, and split inversions
    array_b, x = count_inversions(array[:midpoint])
    array_c, y = count_inversions(array[midpoint:])
    new_array, z = merge_sort_split_array(array_b, array_c)

    total_inversions = x + y + z

    return new_array, total_inversions


def merge_sort_split_array(array_left, array_right):

    n = len(array_right)
    m = len(array_left)
    z = 0
    array_d = []
    i = 0
    j = 0

    while j < n and i < m:
        if array_left[i] < array_right[j]:
            array_d.append(array_left[i])
            i += 1
        elif array_right[j] < array_left[i]:
            array_d.append(array_right[j])
            z += len(array_left) - i
            j += 1
        else:
            array_d.append(array_left[i])
            array_d.append(array_right[j])
            z += len(array_left[i:]) - 1
            i += 1
            j += 1

    # Adds any remaining elements back to array_d
    array_d += array_left[i:]
    array_d += array_right[j:]

    return array_d, z


if __name__ == '__main__':
    main()
