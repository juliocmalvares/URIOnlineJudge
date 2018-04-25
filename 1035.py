data = input()
a = int(data.split()[0])
b = int(data.split()[1])
c = int(data.split()[2])
d = int(data.split()[3])

if b > c and d > a and (c+d) > (a+b) and (c+d) >= 0 and (a+b) >= 0 and a%2 == 0:
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
