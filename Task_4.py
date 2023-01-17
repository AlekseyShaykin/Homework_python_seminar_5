# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


data = open('PYTHON\Homework_seminar_5\\text_in_.txt','r')
for line_0 in data:
    print(line_0)

list_check = list(line_0)

line = line_0.split(',')
print(line)

def Method_zip_in(line):
    lst_len=[]
    for i in line:
     lst_len.append(str(len(i)))
    

    list_zip_in = []
    for i in range(len(lst_len)):
        list_zip_in.append((lst_len[i])+(line[i][:-(len(line[i])-1)]))
    return(list_zip_in)


def Method_zip_out(line):
    lst_numbers=[]
    for i in range(len(line)):      #выводим список из элементов, которые потом преобразуем в число
        lst_numbers.append(line[i][:-1])
    lst_numbers_ = list(map(int,lst_numbers)) #преобразуем элементы в число


    lst_symbol=[]
    for i in range(len(line)):      #выводим список из элементов - переменные (а или b)
        lst_symbol.append(line[i][(len(line[i])-1):])

    lst_summary = list(zip(lst_numbers_,lst_symbol))
    
    list_zip_out=[]
    for i in range(len(lst_summary)):
         list_zip_out.append(lst_summary[i][1]*lst_summary[i][0])
    return(list_zip_out)


count_numb=0                   #опеределяем, ЧТО за текст введен пользователем, чтобы понять - восстанавливать его или сжимать
for i in list_check:
    if i.isdigit():
        count_numb=count_numb +1
    else:
        count_symbol=0
if count_numb>=1:                           # выбираем метод, которые применить к введенному тексту
    lds=[]
    lds = Method_zip_out(line)
    data = open('PYTHON\Homework_seminar_5\\text_out.txt', 'w')   #записываем в файл
    data.writelines(f'{line_0}'+':')
    data.writelines(f'{lds}')
else:
    lds=[]
    lds = Method_zip_in(line)
    data = open('PYTHON\Homework_seminar_5\\text_out.txt', 'w')   #записываем в файл
    data.writelines(f'{line_0}'+' : ')
    data.writelines(f'{lds}')






# data = open('PYTHON\Homework_seminar_5\\text_out.txt', 'w')   #записываем в файл
# data.writelines(f'{line_0}'+':')
# data.writelines(f'{lst_final}')













