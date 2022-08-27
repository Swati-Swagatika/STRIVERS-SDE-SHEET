def merge(intervals):
    if intervals == []:
        return []
    result = []
    intervals.sort()
    print(intervals)
    for ele in intervals:
        if result == [] or result[-1][1] < ele[0]:
            result.append(ele)
        else:
            result[-1][1] = max(result[-1][1], ele[1])
    return result

r, c = map(int, input().split())
matrix = []
for i in range(r):
    arr = []
    for j in range(c):
        arr.append(int(input()))
    print()
    matrix.append(arr)

print(merge(matrix))