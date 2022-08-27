def repeatedNumbers(A):
    n = len(A)
    res = []
    hashmap = {}
    for i in A:
        if i not in hashmap:
            hashmap[i] = True
        else:
            res.append(i)
    for i in range(1, n+1):
        if i not in hashmap:
            res.append(i)
    return res
    
arr = list(map(int, input().split()))
print(repeatedNumbers(arr))
