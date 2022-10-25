# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141.    10^(-1) ≤ d ≤10^(-10)

d=int(input('Введите число : '))
d=d/1000
pi=0
sign=1
x=1
while True:
    a=4/x
    pi+=sign*a
    print(pi)
    if a<=d:
     break
    sign=-sign
    x+=2
    print(f'Множитель = {x}')
print(round(pi,3))
print(d)

