'''
Slelection Sort:
The algorithm goes around the list picking out the smallest
item in the list and putting it at the top.
Time Complexity: O(n^2)
Space Complexity: O(1)
'''


def slectionSort(arr):
    i = 0
    while i < len(arr):
        min = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                index = j
                min = arr[j]
        arr[i], arr[index] = arr[index], arr[i]
        i += 1
    return arr


if __name__ == "__main__":
    num = [32, 43, 32, 1, 23, 21, 465, 987]
    print(slectionSort(num))
    print('fds')