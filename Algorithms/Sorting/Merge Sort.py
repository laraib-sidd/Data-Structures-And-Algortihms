'''
Merge Sort: It uses Divide and Conquer and recursion

Time Complexity : O(n log(n))
Space Complexity : O(n)
'''


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    size = len(arr)
    mid = size / 2
    left = arr[:mid]
    right = arr[mid:]


def merge(left, right):
    pass


if __name__ == "__main__":
    pass
