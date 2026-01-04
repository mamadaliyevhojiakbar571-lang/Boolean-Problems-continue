# Boolean28. x, y sonlar bergan. Jumlani rostlikka tekshiring: "Koordinatalri (x.y) bo'lgan nuqta
# koordinata choragining birinchi yoki uchunchisida yotadi".
x = float(input("x: "))
y = float(input("y: "))
natija = (x > 0 and y > 0) or (x < 0 and y < 0)
print("Natija:", natija)