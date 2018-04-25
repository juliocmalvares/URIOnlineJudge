
valor = int(input())
valor_inicial = valor

nota100 = int(valor/100)
valor = valor - nota100*100
nota50 = int(valor/50)
valor -= nota50*50
nota20 = int(valor/20)
valor -= nota20*20
nota10 = int(valor/10)
valor -= nota10*10
nota5 = int(valor/5)
valor -= nota5*5
nota2 = int(valor/2)
valor-= nota2*2
nota1 = valor
print(valor_inicial)
print("%d nota(s) de R$ 100,00" %nota100)
print("%d nota(s) de R$ 50,00" %nota50)
print("%d nota(s) de R$ 20,00" %nota20)
print("%d nota(s) de R$ 10,00" %nota10)
print("%d nota(s) de R$ 5,00" %nota5)
print("%d nota(s) de R$ 2,00" %nota2)
print("%d nota(s) de R$ 1,00" %nota1)
