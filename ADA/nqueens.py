import numpy as np
print("Enter N")
n=int(input())
count=0
board= np.zeros((n,n),dtype=int)
#print(board)
def issafe(row,col ):
    for i in range(col):
        if board[row][i]==1:
            return False
        
    for k in range(col):
        for j in range(n):
            if k+j==col+row and board[j][k]==1:
                return False
            if k-j==col-row and board[j][k]==1:
                return False
            
    return True

def solve(col):
    if col==n:
        global count
        count+=1
        return
    for i in range(n):
        if issafe(i,col):
            board[i][col]=1
            solve(col+1)
            board[i][col]=0
    return

solve(0)
print("The total number of solutions are: ", count) 



