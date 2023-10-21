row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
board = [row0, row1, row2]

def printBoard():
 print("")
 print(board[0][0], "|", board[0][1], "|", board[0][2])
 print("--+---+--")
 print(row1[0], "|", row1[1], "|", row1[2])
 print("--+---+--")
 print(row2[0], "|", row2[1], "|", row2[2])
 print("")

printBoard()

pos = input("where? ")
pos = int(pos)

row = int((pos - 1) / 3)
column = ((pos - 1) % 3)
print(board[row][column], row, column)