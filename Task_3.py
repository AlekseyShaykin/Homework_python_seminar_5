# Создайте программу для игры в ""Крестики-нолики"".


# lst = [[1,1,1], 
#     [1,1,1], 
#     [1,10,1]]
# print(lst)

# print(lst[2][1])


row = 3
column = 3
A = [[' ']*row for i in range(column)]


# for i in range(len(A)):             #len(A) возвращает кол-во строк в матрице А
#     for j in range(len(A[i])):      # len(A) возращает кол-во эелеентов в СТРОКЕ i
#         print(A[i][j], end =' ')   # то есть матрица записывается слева направо, сверху вниз. end - записываем в отдну строчку элементы через пробел
#     print()                         # делаем переход на новую строку

print(*('0','1','2'))
for row in A:
    print(*row)

    

print('________________')


# row_client = int(input("Введите номер строки: "))
# column_client = int(input("Введите номер ячейки: "))

# A[row_client][column_client] = 'x'

# string = ('0','1','2')
# print(*('0','1','2'))
# for row in A:
#     print(*row)


def Input_row_X():
    row_client_X = int(input("Игрок Х, введите номер строки: "))
    return(row_client_X)
    
def Input_column_X():
    column_client_X = int(input("Игрок Х, введите номер столбца: "))
    return(column_client_X)


def Fill_Player_X_():
    row_client_X = int(input("Игрок Х, введите номер строки: "))
    column_client_X = int(input("Игрок Х, введите номер столбца: "))
    # if A[row_client_X][column_client_X] == 'x' or A[row_client_X][column_client_X] == '0':
    #     print('Эта ячейка уже занята! Введите другие данные')
    #     # row_client_X = Input_row_X
    #     # column_client_X = Input_column_X
    # else:
    #     A[row_client_X][column_client_X] = 'x'

    A[row_client_X][column_client_X] = 'x'
    print(*('0','1','2'))
    for row in A:
        print(*row)
    if A[0][0]=='x' and A[0][1]=='x' and A[0][2]=='x':
     print("Congratulations: X win!")
     print('_______________________')
    elif A[1][0]=='x' and A[1][1]=='x' and A[1][2]=='x':
       print("Congratulations: X win!")
       print('_______________________')  
    elif A[2][0]=='x' and A[2][1]=='x' and A[2][2]=='x':
       print("Congratulations: X win!")
       print('_______________________')
    elif A[0][0]=='x' and A[1][0]=='x' and A[2][0]=='x':
       print("Congratulations: X win!")
       print('_______________________')
    elif A[0][1]=='x' and A[1][1]=='x' and A[2][1]=='x':
       print("Congratulations: X win!")
       print('_______________________')
    elif A[0][2]=='x' and A[1][2]=='x' and A[2][2]=='x':
       print("Congratulations: X win!")
       print('_______________________')
    elif A[0][0]=='x' and A[1][1]=='x' and A[2][2]=='x':
       print("Congratulations: X win!")
       print('_______________________') 
    elif A[0][2]=='x' and A[1][1]=='x' and A[2][0]=='x':
       print("Congratulations: X win!")
       print('_______________________')             
    else:
     row_client_0 = int(input("Игрок 0, введите номер строки: "))
     column_client_0 = int(input("Игрок 0, введите номер столбца: "))
     A[row_client_0][column_client_0] = '0'
   
     print(*('0','1','2'))
    for row in A:
        print(*row)
    if A[0][0]=='0' and A[0][1]=='0' and A[0][2]=='0':
     print("Congratulations: 0 win!")
     print('_______________________') 
    elif A[1][0]=='0' and A[1][1]=='0' and A[1][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')  
    elif A[2][0]=='0' and A[2][1]=='0' and A[2][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
    elif A[0][0]=='0' and A[1][0]=='0' and A[2][0]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
    elif A[0][1]=='0' and A[1][1]=='0' and A[2][1]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
    elif A[0][2]=='0' and A[1][2]=='0' and A[2][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
    elif A[0][0]=='0' and A[1][1]=='0' and A[2][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________') 
    elif A[0][2]=='0' and A[1][1]=='0' and A[2][0]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')             
    else:
        Fill_Player_X_()



Fill_Player_X_()