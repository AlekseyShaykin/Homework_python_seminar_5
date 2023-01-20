# Создайте программу для игры в ""Крестики-нолики"".


# lst = [[1,1,1], 
#     [1,1,1], 
#     [1,10,1]]
# print(lst)

# print(lst[2][1])


row = 3
column = 3
A = [[' ']*row for i in range(column)]

print(*('0','1','2'))
for row in A:
    print(*row)

    

def Input_row_X():
    row_client_X = int(input("Игрок Х, введите номер строки: "))
    return(row_client_X)
    
def Input_column_X():
    column_client_X = int(input("Игрок Х, введите номер столбца: "))
    return(column_client_X)

def Check_win_X(A):
    if A[0][0]=='x' and A[0][1]=='x' and A[0][2]=='x':
     print("Congratulations: X win!")
     print('_______________________')
     exit()
    elif A[1][0]=='x' and A[1][1]=='x' and A[1][2]=='x':
       print("Congratulations: X win!")
       print('_______________________') 
       exit() 
    elif A[2][0]=='x' and A[2][1]=='x' and A[2][2]=='x':
       print("Congratulations: X win!")
       print('_______________________')
       exit()
    elif A[0][0]=='x' and A[1][0]=='x' and A[2][0]=='x':
       print("Congratulations: X win!")
       print('_______________________')
       exit()
    elif A[0][1]=='x' and A[1][1]=='x' and A[2][1]=='x':
       print("Congratulations: X win!")
       print('_______________________')
       exit()
    elif A[0][2]=='x' and A[1][2]=='x' and A[2][2]=='x':
       print("Congratulations: X win!")
       print('_______________________')
       exit()
    elif A[0][0]=='x' and A[1][1]=='x' and A[2][2]=='x':
       print("Congratulations: X win!")
       print('_______________________') 
       exit()
    elif A[0][2]=='x' and A[1][1]=='x' and A[2][0]=='x':
       print("Congratulations: X win!")
       print('_______________________') 
       exit()            
    
def Check_win_0(A):
    if A[0][0]=='0' and A[0][1]=='0' and A[0][2]=='0':
     print("Congratulations: 0 win!")
     print('_______________________')
     exit() 
    elif A[1][0]=='0' and A[1][1]=='0' and A[1][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')  
       exit()
    elif A[2][0]=='0' and A[2][1]=='0' and A[2][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
       exit()
    elif A[0][0]=='0' and A[1][0]=='0' and A[2][0]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
       exit()
    elif A[0][1]=='0' and A[1][1]=='0' and A[2][1]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
       exit()
    elif A[0][2]=='0' and A[1][2]=='0' and A[2][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________')
       exit()
    elif A[0][0]=='0' and A[1][1]=='0' and A[2][2]=='0':
       print("Congratulations: 0 win!")
       print('_______________________') 
       exit()
    elif A[0][2]=='0' and A[1][1]=='0' and A[2][0]=='0':
       print("Congratulations: 0 win!")
       print('_______________________') 
       exit()            

def Fill_Player_X_():

    row_client_X = int(input("Игрок Х, введите номер строки: "))
    column_client_X = int(input("Игрок Х, введите номер столбца: "))
    print('________________')
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
    Check_win_X(A)
       
    row_client_0 = int(input("Игрок 0, введите номер строки: "))
    column_client_0 = int(input("Игрок 0, введите номер столбца: "))
    print('________________')
    A[row_client_0][column_client_0] = '0'
    print(*('0','1','2'))
    for row in A:
        print(*row)
    Check_win_0(A)
    Fill_Player_X_()



Fill_Player_X_()