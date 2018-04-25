pi = 3.14159
a = input()
A = float(a.split()[0])
B = float(a.split()[1])
C = float(a.split()[2])
area = (A*C)/2
print("TRIANGULO: %.3f"%area)
area = (C**2)*pi
print("CIRCULO: %.3f"%area)
area = ((A+B)*C)/2
print("TRAPEZIO: %.3f"%area)
area = (B**2)
print("QUADRADO: %.3f"%area)
area = (B*A)
print("RETANGULO: %.3f"%area)
