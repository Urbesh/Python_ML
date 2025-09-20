#Matrix addition (nested lists)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
print("Enter elements for the first matrix:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Element [{i+1}][{j+1}]: "))
        row.append(val)
    matrix1.append(row)
print("Enter elements for the second matrix:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        val = int(input(f"Element [{i+1}][{j+1}]: "))
        row.append(val)
    matrix2.append(row)
result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("Resultant matrix after addition:")
for row in result:
    print(row)