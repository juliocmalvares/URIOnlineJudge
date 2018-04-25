time = int(input())
h = int(time/3600)
time -= (h*3600)
m = int(time/60)
time -= m*60
s = int(time%60)
print(str(h)+":"+str(m)+":"+str(s))
