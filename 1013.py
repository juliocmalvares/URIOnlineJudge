import math
def f(x,y):
    return int((x+y+int(math.fabs(x-y)))/2)

dados = input()
a = int(dados.split()[0])
b = int(dados.split()[1])
c = int(dados.split()[2])

maior = f(a,b)
maior = f(maior,c)
print("%d eh o maior" % maior)

