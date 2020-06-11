""" Shortcut way
def mergesortedarr(a,b):
x=a+b
x.sort()
return x

a=[1,2,3,4]
b=[3,7,9,12]
qw=mergesortedarr(a,b)
print(qws) """
# In interview we must solve only like this


def mergesortarray(arr1, arr2):
    '''
    Function to implement merge
    '''
    if len(arr1) == 0 or len(arr2) == 0:
        return arr1 + arr2
    mereged_array = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            mereged_array.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            mereged_array.append(arr2[j])
            j += 1
    return mereged_array+arr1[i:]+arr2[j:]


# Driver Code
if __name__ == "__main__":
    a = [1, 3, 4, 6, 20]
    b = [2, 3, 4, 5, 6, 9, 11, 76]
    arr = mergesortarray(a, b)
    print(arr)
