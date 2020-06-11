'''
Insertion Sort

Time Complexity : O(n^2), when the list is almost sorted
the it becomes fast.
Space Complexity : O(1)

'''


def insertionSort(arr):
    size = len(arr)
    i = 1
    end = arr[0]
    while i < size:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0, i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i += 1
    return arr


if __name__ == "__main__":
    num = [12, 32, 3, 53, 98, 8 , 9]
    print(insertionSort(num))
