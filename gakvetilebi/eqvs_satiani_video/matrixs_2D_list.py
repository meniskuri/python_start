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



print("...........................v2.................................")
for row in matrix:
    print(row)
    for item in row:
        print(item)





print("...... list idan unda amovigo ganmeorebadi ricxvebi ......")
numbers = [1, 3, 4, 5, 5, 5, 6, 5, 6, 6, 7, 0, 10, 11, 10, 11]
numbers_chek = []

for i in numbers:
    if i not in numbers_chek:
        numbers_chek.append(i)

print(numbers_chek)
