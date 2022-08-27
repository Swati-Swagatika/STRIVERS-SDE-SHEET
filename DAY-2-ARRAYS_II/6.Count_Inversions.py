def  inversionCount(arr, n):
    res = [0]*n
    return mergeSort(arr,res,0,n-1)

def mergeSort(arr, res, low, high):
    mid = (low+high)//2
    invCount = 0
    if low < high:
        invCount += mergeSort(arr, res, low, mid)
        invCount += mergeSort(arr, res, mid+1, high)
        invCount += merge(arr, res, low, mid, high)
    return invCount

def merge(arr, res, low, mid, high):
    i = k = low
    j = mid + 1
    invCount = 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            res[k] = arr[i]
            k+=1
            i+=1
        else:
            res[k] = arr[j]
            invCount += ((mid-i)+1)
            k+=1
            j+=1
    while i <= mid:
        res[k] = arr[i]
        i+=1
        k+=1
    while j <= high:
        res[k] = arr[j]
        j+=1
        k+=1
    for ele in range(low, high+1):
        arr[ele] = res[ele]
    return invCount


arr = [52244275, 123047899, 493394237, 922363607, 378906890, 188674257, 222477309, 902683641, 860884025, 339100162]
res = inversionCount(arr,len(arr))
print(res)

