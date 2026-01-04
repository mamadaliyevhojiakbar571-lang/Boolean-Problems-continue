# Boolean22. Uch xonali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonning raqamlan ketama-
# ket o'suvchi bo'lib joylashgan yoki kamayuvchi ketma-ketlikka ega".
n = int(input("Uch xonali son: "))
a, b, c = n // 100, (n // 10) % 10, n % 10
print("Natija:", (a < b < c) or (a > b > c))
