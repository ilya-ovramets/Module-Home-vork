#https://repl.it/join/zzdhbhhl-nesterenkov
P = float(input("Введіть Процент-->"))
X = float(input("Введіть рублі-->"))
z = float(input("Введіть копійки-->"))
K = float(input("Введіть кількість років-->"))
Y = z / 100
prk = (X+Y)
proc = (X+Y) /100
vart = proc * P
vars = vart * K
prk = (X+Y) + vars
print("Кінцева сума-->",prk)