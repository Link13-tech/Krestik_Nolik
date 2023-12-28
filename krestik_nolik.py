N = 3
M = 3
A = [["-"]*M for i in range(N)]

for row in A:
    for elem in row:
        print(elem, end=" ")
    print()

for i in range(N):
    for j in range(M):
        A[int(input("Введи строку: "))][int(input("Введи столбец: "))] = input("Введите знак: ")

        for row in A:
            for elem in row:
                print(elem, end=" ")
            print()
if A[0][0] == 'o' and A[0][1] == 'o' and A[0][2] == 'o' or\
           A[1][0] == 'o' and A[1][1] == 'o' and A[1][2] == 'o' or\
           A[2][0] == 'o' and A[2][1] == 'o' and A[2][2] == 'o' or\
           A[0][0] == 'o' and A[1][0] == 'o' and A[2][0] == 'o' or\
           A[0][1] == 'o' and A[1][1] == 'o' and A[2][1] == 'o' or\
           A[0][2] == 'o' and A[1][2] == 'o' and A[2][2] == 'o' or\
           A[0][0] == 'o' and A[1][1] == 'o' and A[2][2] == 'o' or\
           A[2][0] == 'o' and A[1][1] == 'o' and A[0][2] == 'o':
    print("Игрок игравший за нолики выиграл, поздравляю")

elif A[0][0] == 'x' and A[0][1] == 'x' and A[0][2] == 'x' or\
             A[1][0] == 'x' and A[1][1] == 'x' and A[1][2] == 'x' or\
             A[2][0] == 'x' and A[2][1] == 'x' and A[2][2] == 'x' or\
             A[0][0] == 'x' and A[1][0] == 'x' and A[2][0] == 'x' or\
             A[0][1] == 'x' and A[1][1] == 'x' and A[2][1] == 'x' or\
             A[0][2] == 'x' and A[1][2] == 'x' and A[2][2] == 'x' or\
             A[0][0] == 'x' and A[1][1] == 'x' and A[2][2] == 'x' or\
             A[2][0] == 'x' and A[1][1] == 'x' and A[0][2] == 'x':
    print("Игрок игравший за крестики выиграл, поздравляю")

else:
    print("Ничья")