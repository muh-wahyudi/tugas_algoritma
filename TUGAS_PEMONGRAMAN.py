# NAMA:   MUH WAHYUDI
# NIM:    240907501010
# KELAS:  A 


# // Task

# 91 - 100 = A 
# 86 - 90 = A- 
# 81 - 85 = B+ 
# 76 - 80 = B 
# 71 - 75 = B- 
# 66 - 70 = C+ 
# 61 - 65 = C 
# 56 - 60 = C- 
# 51 - 55 = D+ 
# 46 - 50 = D 
# 41 - 45 = D- 
# 0 - 41 = E

# coba buatkan program Nilai Lulus berdasarkan Indeks

A = range(91,101)
B = range(86,91)
C = range(81,86)
D = range(76,81)
E = range(71,76)
F = range(66,71)
G = range(61,66)
H = range(56,61)
I = range(51,56)
J = range(46,51)
K = range(41,51)
L = range(0,41)
nama = input("NAMA: ")
nim = input("NIM: ")
nilai =int(input("masukkan nilai: "))
if (nilai in A):
    print("==========NILAI AKHIR==============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: A")
    print("status: LULUS")
elif (nilai in B):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: A-")
    print("status: LULUS")
elif (nilai in C):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: B+")
    print("status: LULUS")
elif (nilai in D):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: B")
    print("status: LULUS")
elif (nilai in E):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: B-")
    print("status: LULUS")
elif (nilai in F):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: C+")
    print("status: LULUS")
elif (nilai in G):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: C")
    print("status: LULUS")
elif (nilai in H):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: C-")
    print("status: LULUS")
elif (nilai in I):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: D+")
    print("status: TIDAK LULUS")
elif (nilai in J):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: D")
    print("status: TIDAK LULUS")
elif (nilai in K):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: D-")
    print("status: TIDAK LULUS")
elif (nilai in L):
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: E")
    print("status: TIDAK LULUS")
else:
    print("==========NILAI AKHIR============")
    print("NAMA: " + nama)
    print("NIM: " + nim)
    print("index pada semester ini adalah: ERROR")
    print("status: NILAI TIDAK VALID")