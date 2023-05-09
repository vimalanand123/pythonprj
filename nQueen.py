print("this is nQueen program")

for i in range(3,-1,-1):
    print(i)

def isSafe(matrix,row,col):
    #check corresponding columns
    for i in range(col,-1,-1):
        print("is safe", row, i)
        if(matrix[row][i]=='Q'):
            return 0
    for i in range(row-1,-1,-1):
        print("top bottom",i,col)
        if(matrix[i][col]=='Q'):
            return 0
    for i,j in zip(range(row-1,-1,-1), range(col-1,-1,-1)):
        print(i,j)
        if(matrix[i][j]=='Q'):
            return 0

    return(1)
sol = []
poss_no = 0
def nQueen(matrix,row,col):
    if(col>=4):
        global poss_no
        poss_no +=1
        matrixB = [[x for x in rows] for rows in matrix]
        sol.append(matrixB)
        for i in range(8):
            print(matrix[i])
        matrix[row][col - 1] = 0

    for i in range(row,8,1):
        print("row is {} ,col is {} came here".format(i,col))
        if(isSafe(matrix,i,col)):
            print("safe")
            matrix[i][col] = 'Q'

            #back-track for another nQueen
            nQueen(matrix,i,col+1)
        matrix[i][col]  =   0

ChessBoard = [[0 for i in range(8)] for j in range(8)]
#for i in range(8):
nQueen(ChessBoard,0,i)
ChessBoard[6][3] =999
for i in range(poss_no):
    for j in range(8):
        print(sol[i][j],)
    print("********************")