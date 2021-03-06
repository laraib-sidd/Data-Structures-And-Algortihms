'''
Bubble Sort:
The algorithm goes along the values in the list one by one,
if the neighbour is smaller, it switches the position.
It keeps on going untill no switching is found.

Example : [3,1,4]
* First it will compare '3' and '1' as '1' is
smaller it switeches, its positions with '3'.
* Than it checks for '3' and '4', as '4' is already bigger,
no switching.
* As there is no more switching, so the list is sorted.

Time Complexitiy :
Average : O(n^2)

Space Complexity :
O(1)
'''


def bubblsort(arr):
    i = 0
    while i < len(arr):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1
    return arr


# Driver Code
if __name__ == "__main__":
    numbers = [43, 21, 4, 12, 32, 52, 35, 27, 86, 29]
    print(f'Before Sorting : {numbers}')
    bubblsort(numbers)
    print(f'After Sorting : {numbers}')
