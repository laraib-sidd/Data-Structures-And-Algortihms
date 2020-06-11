'''
Slelection Sort:
The algorithm goes around the list picking out the smallest
item in the list and putting it at the top.

'''


def slectionSort(arr):
    smallest = None
    num = []
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[j] < arr[i]:
                smallest = arr[j]
        num.append(smallest)
    return num


if __name__ == "__main__":
    