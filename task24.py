# Boolean24. A, B, C sonlar bellgan (A soni noldan farqli). D=B-4AC diskerminantdan foydalanib,
# jumlani rostlikka tekshiring: "Ax?+Bx+C=0 kvadrat tenglama hagiqiy ildizga ega".
# Boolean24. Kvadrat tenglama haqiqiy ildizga ega
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
D = B**2 - 4*A*C
print("Natija:", D >= 0)