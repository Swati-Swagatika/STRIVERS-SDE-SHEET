class Solution:
    def swap(self, arr, beg, end):
        temp = arr[beg]
        arr[beg] = arr[end]
        arr[end] = temp
    
    def reverse(self, arr, beg, end):
        while beg < end:
            self.swap(arr, beg, end)
            beg += 1
            end -= 1

    def nextPermutation(self, arr):
        if len(arr) == 1:
            return
        if len(arr) == 2:
            self.swap(arr, 0, 1)
        
        dec = len(arr) - 2
        while dec >= 0 and arr[dec] >= arr[dec + 1]:
            dec-=1
        self.reverse(arr, dec+1, len(arr)-1)
        
        if dec == -1:
            return
        next_num = dec + 1
        while next_num < len(arr) and arr[dec] >= arr[next_num]:
            next_num += 1
        
        self.swap(arr, next_num, dec)


arr = list(map(int, input().split()))
ob = Solution()
sol = ob.nextPermutation(arr)
for i in arr:
    print(i, end=" ")
