def generate(numRows):
    triangle = [[1]*i for i in range(1, numRows+1)]
    i = 1
    while i < numRows:
        for j in range(1, len(triangle[i-1])):
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
        i+=1
    return triangle

print(generate(int(input())))
n = int(input())
k = n-1
for i in range(n):
    num=1
    for j in range(0, k):
        print(end=" ")
    k = k-1
    for j in range(0, i+1):
        print(num, end=" ")
        num += 1
    print('\r')
