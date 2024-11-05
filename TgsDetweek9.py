#KE 1 ~ (2x2)
print("masukkan elemen-elemen matriks 2x2: ")
matriks_2x2 = []
for i in range(2):
    row = []
    for j in range(2):
        value = int(input(f"elemen [{i}][{j}]: "))
        row.append(value)
    matriks_2x2.append(row)


deter_2x2 = matriks_2x2[0][0] * matriks_2x2[1][1] - matriks_2x2[0][1] * matriks_2x2[1][0]
print("determinan 2x2: ", deter_2x2)


#KE 2 ~ (3x3)
print("\nmasukkan elemen-elemen matriks 3x3:")
matriks_3x3 = []
for i in range(3):
    row = []
    for j in range(3):
        value = int(input(f"elemen [{i}][{j}]: "))
        row.append(value)
    matriks_3x3.append(row)


deter_3x3 = (matriks_3x3[0][0] * (matriks_3x3[1][1] * matriks_3x3[2][2] - matriks_3x3[1][2] * matriks_3x3[2][1])
           - matriks_3x3[0][1] * (matriks_3x3[1][0] * matriks_3x3[2][2] - matriks_3x3[1][2] * matriks_3x3[2][0])
           + matriks_3x3[0][2] * (matriks_3x3[1][0] * matriks_3x3[2][1] - matriks_3x3[1][1] * matriks_3x3[2][0]))
print("determinan 3x3:", deter_3x3)


#KE 3 ~ (4x4)
print("\nmasukkan elemen-elemen matriks 4x4:")
matriks_4x4 = []
for i in range(4):
    row = []
    for j in range(4):
        value = int(input(f"elemen [{i}][{j}]: "))
        row.append(value)
    matriks_4x4.append(row)


deter_4x4 = (matriks_4x4[0][0] * (matriks_4x4[1][1] * (matriks_4x4[2][2] * matriks_4x4[3][3] - matriks_4x4[2][3] * matriks_4x4[3][2])
                               - matriks_4x4[1][2] * (matriks_4x4[2][1] * matriks_4x4[3][3] - matriks_4x4[2][3] * matriks_4x4[3][1])
                               + matriks_4x4[1][3] * (matriks_4x4[2][1] * matriks_4x4[3][2] - matriks_4x4[2][2] * matriks_4x4[3][1]))
           - matriks_4x4[0][1] * (matriks_4x4[1][0] * (matriks_4x4[2][2] * matriks_4x4[3][3] - matriks_4x4[2][3] * matriks_4x4[3][2])
                               - matriks_4x4[1][2] * (matriks_4x4[2][0] * matriks_4x4[3][3] - matriks_4x4[2][3] * matriks_4x4[3][0])
                               + matriks_4x4[1][3] * (matriks_4x4[2][0] * matriks_4x4[3][2] - matriks_4x4[2][2] * matriks_4x4[3][0]))
           + matriks_4x4[0][2] * (matriks_4x4[1][0] * (matriks_4x4[2][1] * matriks_4x4[3][3] - matriks_4x4[2][3] * matriks_4x4[3][1])
                               - matriks_4x4[1][1] * (matriks_4x4[2][0] * matriks_4x4[3][3] - matriks_4x4[2][3] * matriks_4x4[3][0])
                               + matriks_4x4[1][3] * (matriks_4x4[2][0] * matriks_4x4[3][1] - matriks_4x4[2][1] * matriks_4x4[3][0]))
           - matriks_4x4[0][3] * (matriks_4x4[1][0] * (matriks_4x4[2][1] * matriks_4x4[3][2] - matriks_4x4[2][2] * matriks_4x4[3][1])
                               - matriks_4x4[1][1] * (matriks_4x4[2][0] * matriks_4x4[3][2] - matriks_4x4[2][2] * matriks_4x4[3][0])
                               + matriks_4x4[1][2] * (matriks_4x4[2][0] * matriks_4x4[3][1] - matriks_4x4[2][1] * matriks_4x4[3][0])))
print("determinan 4x4:", deter_4x4)