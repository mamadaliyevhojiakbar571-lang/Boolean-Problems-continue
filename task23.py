# Boolean23. Uch xonali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonni chapdan o'qiganda
# ham, o'ngdan o'giganda ham bir xil".
n = int(input("Uch xonali son: "))
a, b, c = n // 100, (n // 10) % 10, n % 10
print("Natija:", a == c)