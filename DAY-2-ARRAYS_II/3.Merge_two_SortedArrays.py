def merge(num1, num2, m, n):
    last = m + n - 1
    while m > 0 and n > 0:
        if num1[m - 1] > num2[n-1]:
            num1[last] = num1[m - 1]
            m -= 1
        else:
            num1[last] = num2[n - 1]
            n -= 1 
        last -= 1
    while n > 0:
        num1[last] = num2[n - 1]
        n -= 1
        last -= 1
    return num1
            
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, nums2, m, n))