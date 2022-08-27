def rotateImage(matrix):
    N = len(matrix[0])
    for i in range(N//2):
        for j in range(i, N-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[N-1-j][i]
            matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
            matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
            matrix[j][N-1-i] = temp

r, c = map(int, input().split())
matrix = []
for i in range(r):
    arr = []
    for j in range(c):
        arr.append(int(input()))
    print()
    matrix.append(arr)
rotateImage(matrix)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()