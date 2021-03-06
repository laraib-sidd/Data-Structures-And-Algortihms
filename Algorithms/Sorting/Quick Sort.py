"""
Quick Sort:
This function takes last element as pivot, places
the pivot element at its correct position in sorted
array, and places all smaller (smaller than pivot)
to left of pivot and all greater elements to right
of pivot.

Time Complexity : O(n log(n))
Space Complexity : O(n log(n))
"""


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element.
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index


# Function to do Quick Sort
def quicksort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)


if __name__ == "__main__":
    arr = [12, 4, 2, 3, 7, 43, 87, 9, 5]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print(arr)
