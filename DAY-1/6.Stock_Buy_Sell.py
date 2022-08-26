def stockSell(prices):
    maxPrice = float('inf')
    maxProfit = 0
    for price in prices:
        maxPrice = min(maxPrice, price)
        profit = price - maxPrice
        maxProfit = max(maxProfit, profit)
    return maxProfit

prices = list(map(int, input().split()))
print(stockSell(prices))

def swap(arr, p, q):
    temp = arr[p]
    arr[p] = arr[q]
    arr[q] = temp

x, k = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(k):
    p,q = map(int, input().split())
    swap(arr,p-1,q-1)
print(arr)