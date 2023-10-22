# Creates a board with three rows
row0 = [" ", " ", " "]
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
board = [row0, row1, row2]

# Prints the board
def printBoard(board):
 print("")
 print(board[0][0], "|", board[0][1], "|", board[0][2])
 print("--+---+--")
 print(board[1][0], "|", board[1][1], "|", board[1][2])
 print("--+---+--")
 print(board[2][0], "|", board[2][1], "|", board[2][2])
 print("")

printBoard(board)

playerTurn = "X"

# Repeats forever
while True:
 pos = input(playerTurn + " is up, what square will you play? ")
 if pos == "stop":
   print("")
   print("")
   print("")
   print("")
   print("You have ended the game. Final Board:")
   printBoard(board)
   break # Stops the forever loop with the keyword
 else:
  pos = int(pos)
 
  row = int((pos - 1) / 3)
  column = ((pos - 1) % 3)
  board[row][column] = playerTurn

  printBoard(board)

  # Switches playerTurn between "X" and "O"
  if playerTurn == "X":
   playerTurn = "O"
  else:
   playerTurn = "X"