matrix = [
    [1,2,3],
    [4,5,6]
]
print("len is ", len(matrix[1]))
print("len is ", len(matrix))
k = 0
p = 0
for i in matrix:
    print("p =     ",p)
    k = 0
    for j in matrix[1]:
        print("k =                  ",k)
        print("matrix[p][k] =                ",matrix[p][k] + 4)
        k = k + 1
    p = p + 1
