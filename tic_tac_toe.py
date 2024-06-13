# Creates a board with three rows
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Keeps track of the score
score = {"X": 0, "O": 0}

# Prints the board
def printBoard(board):
  print("")
  print(board[0][0], "|", board[0][1], "|", board[0][2])
  print("--+---+--")
  print(board[1][0], "|", board[1][1], "|", board[1][2])
  print("--+---+--")
  print(board[2][0], "|", board[2][1], "|", board[2][2])
  print("")

# Starts the game
def playGame():

  printBoard([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])

  # Resets the board
  board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

  playerTurn = "X"

  while True: # Repeats until a break keyword is used
    try:
      pos = int(input(playerTurn + " is up, what square will you play? "))
    except ValueError: # if input cannot be converted to int
        print("Please enter a number")
    else:
      if pos == 0:
        print("")
        print("")
        print("")
        print("")
        print("You have ended the game. Final Board:")
        printBoard(board)
        break # Stops the forever loop with the keyword
      else:
        row = int((pos - 1) / 3)
        column = (pos - 1) % 3

        if pos in list(range(1,10)): # Checks if input is 1-9

          if board[row][column] == " ": # Checks if the space has been played on
            board[row][column] = playerTurn

            printBoard(board)

            # Detects if there is a winner

            # Checks rows
            if board[row][0] == playerTurn and board[row][1] == playerTurn and board[row][2] == playerTurn:
              print(playerTurn, "wins on row", str((row + 1)) + "!")
              score[playerTurn] += 1
              break

            # Checks columns
            if board[0][column] == playerTurn and board[1][column] == playerTurn and board[2][column] == playerTurn:
              print(playerTurn, "wins on column", str((column + 1)) + "!")
              score[playerTurn] += 1
              break

            # Checks diagonals
            if board[0][0] == playerTurn and board[1][1] == playerTurn and board[2][2] == playerTurn:
              print(playerTurn, "wins on a diagonal!")
              score[playerTurn] += 1
              break
            if board[0][2] == playerTurn and board[1][1] == playerTurn and board[2][0] == playerTurn:
              print(playerTurn, "wins on a diagonal!")
              score[playerTurn] += 1
              break

            # Checks for a tie
            if " " not in board[0] and " " not in board[1] and " " not in board[2]:
              print("No one wins! It's a tie!")
              break

            # Switches playerTurn between "X" and "O"
            if playerTurn == "X":
              playerTurn = "O"
            else:
              playerTurn = "X"
          else:
            print(board[row][column], "is already there.")
        else:
          print("Please enter a number that is 1-9.")

  # Displays the score
  print("")
  print("The score is currently:")
  print("X:", score["X"])
  print("O:", score["O"])
  print("")

playGame()

# Play again?
while True:

  playAgain = input("Do you want to play again? ")
  if playAgain == "y":
    playGame()
  elif playAgain == "n":
    print("Thanks for playing!")
    break
  else:
    print("Please enter 'y' or 'n'.")
