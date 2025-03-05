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

A = list(range(91,101))
B = list(range(86,91))
C = list(range(81,86))
D = list(range(76,81))
E = list(range(71,76))
F = list(range(66,71))
G = list(range(61,66))
H = list(range(56,61))
I = list(range(51,56))
J = list(range(46,51))
K = list(range(41,51))
L = list(range(41))
nilai =int(input("masukkan nilai: "))
if (nilai in A):
    print("nilai anda pada semester ini adalah: A")
    print("anda LULUS")
elif (nilai in B):
    print("nilai anda pada semester ini adalah: A-")
    print("anda LULUS")
elif (nilai in C):
    print("nilai anda pada semester ini adalah: B+")
    print("anda LULUS")
elif (nilai in D):
    print("nilai anda pada semester ini adalah: B")
    print("anda LULUS")
elif (nilai in E):
    print("nilai anda pada semester ini adalah: B-")
    print("anda LULUS")
elif (nilai in F):
    print("nilai anda pada semester ini adalah: C+")
    print("anda LULUS")
elif (nilai in G):
    print("nilai anda pada semester ini adalah: C")
    print("anda LULUS")
elif (nilai in H):
    print("nilai anda pada semester ini adalah: C-")
    print("anda LULUS")
elif (nilai in I):
    print("nilai anda pada semester ini adalah: D+")
    print("anda TIDAK LULUS")
elif (nilai in J):
    print("nilai anda pada semester ini adalah: D")
    print("anda TIDAK LULUS")
elif (nilai in K):
    print("nilai anda pada semester ini adalah: D-")
    print("anda TIDAK LULUS")
elif (nilai in L):
    print("nilai anda pada semester ini adalah: E")
    print("anda TIDAK LULUS")
else:
    print("ERROR")