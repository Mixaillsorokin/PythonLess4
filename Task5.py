# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open ('Task5_REZULT.txt','w') as date:
    date1=open('Task5_1.txt','r') 
    date2=open('Task5_2.txt','r')
    for line1 in date1:
        for line2 in date2:
            date.write(str(line1) + str(line2))


