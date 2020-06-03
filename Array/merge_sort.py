def mergesortarray(arr1,arr2):

    if len(arr1)==0 or len(arr2)==0:
        return arr1 + arr2
    
    mereged_array = []
    i = 0
    j = 0
    
    while i<len(arr2) or j < len(arr2):
        if arr1[i]<=arr2[j]:
            mereged_array.append(arr1[i])
            i+=1
        
        elif arr1[i] >= arr2[j]:
            mereged_array.append(arr2[j])
            j+=1      

    return mereged_array