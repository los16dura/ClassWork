def myPrint(m):
    for i in m:
        print(*i)
    print()
def dist(first, second):
    matrix =[[0]*(len(second) + 1) for i in range(len(first) + 1)]
    for i in range(len(first) + 1):
        matrix[i][0] = i
    for i in range(len(second) + 1):
        matrix[0][i] = i

    for i in range(1, len(first) + 1):
        for j in range(1,len(second) + 1):
            matrix[i][j] = min(
                matrix[i][j-1] + 1,
                matrix[i-1][j] + 1,
                matrix[i-1][j-1] + (0 if first[i-1] == second[j-1] else 1)
            )
    return matrix[-1][-1]


first = input()
second = input()

print(dist(first,second))