def duplicateNum(nums):
    hashMap = {}
    res = []
    for ele in nums:
        indCount = hashMap.get(ele)
        if indCount:
            hashMap[ele] = indCount + 1
        else:
            hashMap[ele] = 1

    for keys, values in hashMap.items():
        if values > 1:
            res.append(keys)
    if len(hashMap) == 0:
        return
    else:
        res.sort()
    for x in res:
        print(x, end=" ")

nums = [1,3,3,7,2,2]
duplicateNum(nums)
