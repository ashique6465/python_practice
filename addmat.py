
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[9, 8, 7],
     [6, 5, 4]]


res = []
for i in range(len(A)):
    row = []
    for j in range(len(B)):
        row.append(A[i][j] + B[i][j])
    res.append(row)
print(res)