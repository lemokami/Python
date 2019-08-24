#print board function to print the board
def printboard(board):
    print(board[1]+' | '+ board[2] + ' | ' + board[3])
    print("----------")
    print(board[4]+' | '+ board[5] + ' | ' + board[6])
    print("----------")
    print(board[7]+' | '+ board[8] + ' | ' + board[9])


checkboard = dict() #making the board

for i in range(10): #using range to make the desired dictionary for the board
    checkboard.setdefault(i,' ')

printboard(checkboard)


#More Needed