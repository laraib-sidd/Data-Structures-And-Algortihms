'''
Merge Sort: It uses Divide and Conquer and recursion

Time Complexity : O(n log(n))
Space Complexity : O(n)
'''


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    size = len(arr)
    mid = size // 2
    left = arr[:mid]
    right = arr[mid:]
    print(f'Left : {left}')
    print(f'Right : {right}')

    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    res = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            res.append(left[leftindex])
            leftindex += 1
        else:
            res.append(right[rightindex])
            rightindex += 1
        print(left, right)
        print(res + left[leftindex:] + right[rightindex:])
        return res + left[leftindex:] + right[rightindex:]


if __name__ == "__main__":
    num = [1, 34, 76, 9, 23, 912, 6, 36]
    print(mergeSort(num))
