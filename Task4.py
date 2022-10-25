# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k=int(input())
KmN=[]
for i in range(k+1):
    KmN.append(random.randint(1,99))
print(KmN)
ForFile=''
for i in range(len(KmN)-1):
    if KmN[i]!=0:
        if(k-i)==1:
            ForFile+=str(KmN[i])+'x + '
        else:
            f=int(k-i)
            ForFile+=str(KmN[i])+'x'+'^'+str(f)+' + '

ForFile+=str(KmN[-1])+' = 0'

with open('Task4.txt', 'w+') as date:
    date.write(ForFile)

print(ForFile)