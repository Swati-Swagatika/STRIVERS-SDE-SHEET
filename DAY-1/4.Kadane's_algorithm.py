def maxSubarraySum(arr):
    maximum = max(arr)
    if maximum < 0:
        return maximum
    maxEnding = 0
    maxSoFar = 0
    for i in arr:
        maxEnding = maxEnding + i
        maxEnding = max(maxEnding, 0)
        maxSoFar = max(maxEnding, maxSoFar)
    return maxSoFar

arr = list(map(int, input().split()))
print(maxSubarraySum(arr))
