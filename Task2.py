# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('N :'))
numlist=[]
for i in range(1,N):
    if (N % i==0):
        if(i% i==0)and(i%1==0):
            numlist.append(i)
print(f'Простые множетели N-го числа => {numlist}')