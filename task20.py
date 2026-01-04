# Boolean20. Uch xonali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonning barcha ragamlari xar
# xil".
n = int(input("Uch xonali son: "))
a, b, c = n // 100, (n // 10) % 10, n % 10
print("Natija:", a != b and b != c and a != c)