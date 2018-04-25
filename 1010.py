a = input()
b = input()

prim = [p for p in a.split()]
seg = [p for p in b.split()]
prim[0] = int(prim[0])
prim[1] = int(prim[1])
prim[2] = float(prim[2])
seg[0] = int(seg[0])
seg[1] = int(seg[1])
seg[2] = float(seg[2])

total = (prim[1]*prim[2])+(seg[1]*seg[2])
print("VALOR A PAGAR: R$ %.2f" % total)
