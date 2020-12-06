#https://repl.it/join/zzdhbhhl-nesterenkov
x1=int(input('Введіть число 1:'))
x2=int(input('Введіть число 2:'))
x3=int(input('Введіть число 3:'))
x4=int(input('Введіть число 4:'))

if x1 % 2 == 1 or x2 % 2 == 1:
  if x3 % 2 == 1 or x4 % 2 == 1:
    if x1 % 2 == 0 or x2 % 2 == 0:
      if x3 % 2 == 0 or x4 % 2 == 0:
        print("YES")
      else:
        print("NO")		