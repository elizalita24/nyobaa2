#deklarasi variabel 
var_nilai = 0

while (var_nilai < 10) :
    print("perulangan ke ", var_nilai,"(",var_nilai,"antara 0 sampai 10)Bernilai True")
    var_nilai +=1

#diluar perulangan
print("var_nilai = ",int(var_nilai)," = 10. bernilai false")

#for dengan 1 argumen 

for x in range (5) :
    print (x)

#for dengan 2 argumen 

for z in range (8,10) :
    print (z)

#for dengan 3 argumen

for y in range(1,20,2):
    print (y)

#for untuk menghitung mundur

for u in range (20,1,-3):
    print(u)

#perulangan dalam string

for t in "informatika UKWMS":
    print(t)

#menghilangkan 
tandabaca = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

teks = str(input("Masukkan kalimat dengan tanda baca : "))
kata = ""
for char in teks:
    if char not in tandabaca:
        kata = kata + char
print(kata)

#coba

for i in range(2):
    print(f'perulangan luar[{i}]=',i)
    for j in range(10):
        print(f'perulangan dalam[{i},{j}]=',str(i)+','+str(j))

#percobaan perulangan 

for y in range(3):
    print(f'perulangan luar[{y}]=', y)
    for t in range(9):
        print(f'perulangan dalam[{y},{t}]=',str(y)+','+str(t))

#percobaan 

pertama = int(input("Masukkan jumlah perulangan luar = "))
kedua = int(input("Masukkan jumlah perulangan kedua = "))

for i in range(pertama):
    print(f'perulangan luar[{i}]=',i)
    for j in range(kedua):
        print(f'perulangan dalam[{i},{j}]=',str(i)+','+str(j))