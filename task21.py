# Boolean21. Uch xonali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonning raqamlari ketama-
# ket o'suvchi bo'lib joylashgan".
n = int(input("Uch xonali son: "))
a, b, c = n // 100, (n // 10) % 10, n % 10
print("Natija:", a < b and b < c)