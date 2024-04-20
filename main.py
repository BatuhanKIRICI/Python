def paint_calc(h, w, c):
    print(round((h * w) / c))


coverage = 5

height = int(input("Height? "))
width = int(input("Width? "))

paint_calc(w=width, c=coverage, h=height)
