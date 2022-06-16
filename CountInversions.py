"""
Stanford - Divide and Conquer Algorithms - Challenge 2
by James Kwon Lee (6.15.22)

Task: Count Inversions from a list of numbers generated from a .txt file.
- Create a Divide and Conquer Algorithm
- Running time should be approx. O(n) = n log n or faster

Pseudocode for counting Split-Inversions:
- Sort the left and right arrays, then merge into a new array, D.
- While sorting,
    if left array element is larger than right array element,
        the remaining elements of the left array count towards split-inversion count.

"""


def main():
    array_a = open("IntegerArray.txt").readlines()
    array_a = list(map(int, array_a))

    sorted_b, x = count_and_sort_b(array_a)
    sorted_c, y = count_and_sort_c(array_a)
    z = merge_split_array(sorted_b, sorted_c)

    total_inversions = x + y + z
    print("total_inversions: ", total_inversions)
    return total_inversions


def count_and_sort_b(array):
    n = len(array)//2
    array_b = array[:n]

    if n <= 1:
        return array_b, 0

    x = 0

    for i in range(0, len(array_b) - 1):
        for j in range(i + 1, len(array_b)):
            if array_b[j] < array_b[i]:
                x += 1
    sort(array_b)

    return array_b, x


def count_and_sort_c(array):
    n = len(array) // 2
    array_c = array[n:]

    if n <= 1:
        return array_c, 0

    y = 0

    for i in range(0, len(array_c) - 1):
        for j in range(i + 1, len(array_c)):
            if array_c[i] > array_c[j]:
                y += 1

    sort(array_c)

    return array_c, y


def sort(array):
    # update with a faster sorting algorithm in the future
    sorted_array = array.sort()

    return sorted_array


def merge_split_array(sorted_left, sorted_right):

    n = len(sorted_right)
    m = len(sorted_left)
    z = 0
    array_d = []
    i = 0
    j = 0

    while j < n and i < m:
        if sorted_left[i] < sorted_right[j]:
            array_d.append(sorted_left[i])
            i += 1
        elif sorted_right[j] < sorted_left[i]:
            array_d.append(sorted_right[j])
            z += len(sorted_left[i:])
            j += 1
        else:
            array_d.append(sorted_left[i])
            array_d.append(sorted_right[j])
            z += len(sorted_left[i:]) - 1
            i += 1
            j += 1

    return z


if __name__ == '__main__':
    main()
