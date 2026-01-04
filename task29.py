# Boolean29. (x. y). (x1, y1), (x2, y2) sonlari berilgan. Jumlani rostlikka tekshiring: "Koordinatalari (x.y)
# bo'lgan nuqta, chap yuqori cho'qqisi (x1,y1) koordinatalarga ega bo'lgan va o'ng pastikisi (x2,y2)
# bo'lgan, tomonlari esa koordinata o'glariga parallel bo'igan to'rtburchak ichida yotadi"
x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))
x, y = float(input("x: ")), float(input("y: "))
natija = (x1 <= x <= x2) and (y2 <= y <= y1)
print("Natija:", natija)
