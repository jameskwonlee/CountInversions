# Count Inversions

by James Kwon Lee (06.15.22)

### Introduction: 
- <strong>Inversions</strong> in a sequence is a pair of elements that are out of their natural order (in our case, out of chronological order). 
- Could be used to compare two or more data sets and see how (dis)similar they are (i.e. might be utilized in Netflix's film recommender or Eharmony's compatibility filters, etc.)
- A brute force method can compare each element in the array against itself but leads to a quadratic or slower running time. 
- A divide and conquer algorithm allows for the program to run O(n log n) time.

### About The Code:
- Written in Python, I split the array into the left and right array halves and count the number of inversions for each. 
- To count the split inversions, I sort each of the halves, and then merge them into a new array D. 
- While iterating through each of the sorted arrays, if the left array element is greater than the right, the remaining elements in the left array contribute towards the split array count.

### Instructions:
- In console, type: `python CountInversions.py` to run code.

### Future direction:
- In my next pass, I need to call the left and right array count functions recursively. 
- Sorting seems implicit when Merge_Sort_Split_Array is called, so there's no need to do it within the left and right functions. 
- I'd like to explore different data structures to organize and sort the large list of numbers. 
