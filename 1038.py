preco = [4.0, 4.5, 5.0, 2.0, 1.5]

data = input()
cod = int(data.split()[0])
qtd = int(data.split()[1])
total = 0
cod -= 1
for i in range(qtd):
	total += preco[cod]
print("Total: R$ %.2f" % total)
