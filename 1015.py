import math
def dist(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

a = input()
b = input()
x1 = float(a.split()[0])
y1 = float(a.split()[1])
x2 = float(b.split()[0])
y2 = float(b.split()[1])

print("%.4f"%dist(x1,x2,y1,y2))

