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

printBoard([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

playerTurn = "X"

while True: # Repeats forever
  try:
    pos = int(input(playerTurn + " is up, what square will you play? "))
  except ValueError: # if input cannot be converted to int
    if pos == "stop":
      print("")
      print("")
      print("")
      print("")
      print("You have ended the game. Final Board:")
      printBoard(board)
      break # Stops the forever loop with the keyword
    else:
      print("Please enter a number")
  else:
    row = int((pos - 1) / 3)
    column = (pos - 1) % 3
  
    if pos in list(range(1,10)): # Checks if input is 1-9

      if board[row][column] == " ": # Checks if the space has been played on
        board[row][column] = playerTurn

        printBoard(board)

        # Switches playerTurn between "X" and "O"
        if playerTurn == "X":
          playerTurn = "O"
        else:
          playerTurn = "X"
      else:
        print(board[row][column], "is already there.")
    else:
      print("Please enter a number that is 1-9.")