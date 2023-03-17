empty_board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]  
divider = "-+-+-"
board_index = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print(divider)
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print(divider)
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def player_one_choice():
    print("Player One, make your move and enter a number between 1 & 9:")
    move = int(input())
    if move == 1 and empty_board[0][0] == ".":
        empty_board[0][0] = "X"
    elif move == 2 and empty_board[0][1] == ".":
        empty_board[0][1] = "X"
    elif move == 3 and empty_board[0][2] == ".":
        empty_board[0][2] = "X"
    elif move == 4 and empty_board[1][0] == ".":
        empty_board[1][0] = "X"
    elif move == 5 and empty_board[1][1] == ".":
        empty_board[1][1] = "X"
    elif move == 6 and empty_board[1][2] == ".":
        empty_board[1][2] = "X"
    elif move == 7 and empty_board[2][0] == ".":
        empty_board[2][0] = "X"
    elif move == 8 and empty_board[2][1] == ".":
        empty_board[2][1] = "X"
    elif move == 9 and empty_board[2][2] == ".":
        empty_board[2][2] = "X"
    else:
        print("Error. Please enter a number between 1 and 9 that isn't already taken")

def player_two_choice():
    print("Player Two, make your move and enter a number between 1 & 9:")
    move = int(input())
    if move == 1 and empty_board[0][0] == ".":
        empty_board[0][0] = "0"
    elif move == 2 and empty_board[0][1] == ".":
        empty_board[0][1] = "0"
    elif move == 3 and empty_board[0][2] == ".":
        empty_board[0][2] = "0"
    elif move == 4 and empty_board[1][0] == ".":
        empty_board[1][0] = "0"
    elif move == 5 and empty_board[1][1] == ".":
        empty_board[1][1] = "0"
    elif move == 6 and empty_board[1][2] == ".":
        empty_board[1][2] = "0"
    elif move == 7 and empty_board[2][0] == ".":
        empty_board[2][0] = "0"
    elif move == 8 and empty_board[2][1] == ".":
        empty_board[2][1] = "0"
    elif move == 9 and empty_board[2][2] == ".":
        empty_board[2][2] = "0"
    else:
        print("Error. Please enter a number between 1 and 9 that isn't already taken")

def check_winner():
  i = 0
  if empty_board[0][0] == "X" and empty_board[0][1] == "X" and empty_board[0][2] == "X":
    i += 1
  elif empty_board[1][0] == "X" and empty_board[1][1] == "X" and empty_board[1][2] == "X":
    i += 1
  elif empty_board[2][0] == "X" and empty_board[2][1] == "X" and empty_board[2][2] == "X":
    i += 1
  elif empty_board[0][0] == "X" and empty_board[1][1] == "X" and empty_board[2][2] == "X":
    i += 1
  elif empty_board[0][2] == "X" and empty_board[1][1] == "X" and empty_board[2][0] == "X":
    i += 1
  elif empty_board[0][0] == "X" and empty_board[1][0] == "X" and empty_board[2][0] == "X":
    i += 1
  elif empty_board[0][1] == "X" and empty_board[1][1] == "X" and  empty_board[2][1] == "X":
    i += 1
  elif empty_board[0][2] == "X" and empty_board[1][2] == "X" and empty_board[2][2] == "X":
    i += 1
  elif empty_board[0][0] == "O" and empty_board[0][1] == "O" and empty_board[0][2] == "O":
    i += 1
  elif empty_board[1][0] == "O" and empty_board[1][1] == "O" and empty_board[1][2] == "O":
    i += 1
  elif empty_board[2][0] == "O" and empty_board[2][1] == "O" and empty_board[2][2] == "O":
    i += 1
  elif empty_board[0][0] == "O" and empty_board[1][1] == "O" and empty_board[2][2] == "O":
    i += 1
  elif empty_board[0][2] == "O" and empty_board[1][1] == "O" and empty_board[2][0] == "O":
    i += 1
  elif empty_board[0][0] == "O" and empty_board[1][0] == "O" and empty_board[2][0] == "O":
    i += 1
  elif empty_board[0][1] == "O" and empty_board[1][1] == "O" and  empty_board[2][1] == "O":
    i += 1
  elif empty_board[0][2] == "O" and empty_board[1][2] == "O" and empty_board[2][2] == "O":
    i += 1
  else:
     pass
  return i

#game
def play_game():
  print("Tic Tac Toe. Take it in turns to pick a square and try and get three in a row before your opponent. Here's the board reference:")
  board(board_index)

  
  player_one_choice()

  print("Current state of the board:")
  board(empty_board)

  player_two_choice()
