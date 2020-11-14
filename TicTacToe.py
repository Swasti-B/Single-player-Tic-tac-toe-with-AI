import math

board = [' ' for x in range(10)]
board[0] = -1

#inserts the letter in the gameboard everytime a position of theri leter is chosen by the player
def LetterInsert(letter,pos):
  board[pos]= letter

#checks if the entered position is available in the board
def SpaceFree(User_move):
    if board[User_move] == ' ':
      return True 
    else:
      return False

def DisplayBoard():
  print(board[1]+" | "+board[2]+" | "+board[3])
  print("---------")
  print(board[4]+" | "+board[5]+" | "+board[6])
  print("---------")
  print(board[7]+" | "+board[8]+" | "+board[9])


def isWinner(bo,value):
  return(bo[7]==value and bo[8]==value and bo[9]==value)or(bo[4]==value and bo[5]==value and bo[6]==value) or(bo[1]==value and bo[2]==value and bo[3]==value) or(bo[1]==value and bo[4]==value and bo[7]==value) or(bo[2]==value and bo[5]==value and bo[8]==value) or(bo[3]==value and bo[6]==value and bo[9]==value) or(bo[1]==value and bo[5]==value and bo[9]==value) or(bo[3]==value and bo[5]==value and bo[7]==value)

def game_over(state):
  if isWinner(state,'X') or isWinner(state,'O') or BoardFullCheck(state):
    return True
  else:
    return False

#Execution of X player i.e human player 
def PlayersMove():
  check = True
  while check:
    User_move = input("Please choose your position for 'X' (1-9):")
    if User_move == "Quit" or User_move=="quit":
        exit()
        break
    try:
      User_move = int(User_move)
      if User_move >0 and User_move<10:
        if SpaceFree(User_move):
          check = False
          LetterInsert('X',User_move)
        else:
          print("Sorry the space is occupied!")
      else:
        print("Please insert the position within the range.")
    except:
        print("Please insert the valid position!")

#for a certain state, checks for the total possible move and returns the list of the position available
def AvailableMoves(state):
  enumeratedList =[i for i,l in enumerate(state) if l== " "]
  return enumeratedList

#returns utility values
def Utility_list(Move_list):
  if isWinner(Move_list,'X'):
    return -1
  elif isWinner(Move_list,'O'):
    return 1
  else:
    return 0

#best stores the index of parent of the best node into position 0 and its utility value into position 1
def Max_val(depth,state):
  best = [-1,-math.inf]
  if(depth==0 or game_over(state)):
    Utility_val = Utility_list(state)
    return(state[0],Utility_val)
  available_spot = AvailableMoves(state)
  for i in available_spot:
    state[0] = i  #state's first element contains the index of its parent, or which available space did it came from
    state[i]= "O"
    value = Min_val(depth-1,state)
    state[i]= " "
    if value[1] > best[1]:
      best[1] = value[1]
      best[0] = i
  return best

def Min_val(depth,state):
  best = [-1,math.inf]
  if(depth==0 or game_over(state)):
    Utility_val = Utility_list(state)
    return(state[0],Utility_val)
  available_spot = AvailableMoves(state)
  for i in available_spot:
    state[0] = i  #state's first element contains the index of its parent, or which available space did it came from
    state[i]= "X"
    value = Max_val(depth-1,state)
    state[i]= " "
    if value[1]<best[1]:
      best[1] = value[1]
      best[0] = i
  return best

#Execution of Computer's move
def compMove():
  boardCopy = board
  depth = len(AvailableMoves(boardCopy)) 
  comp_move = Max_val(depth, boardCopy)
  return comp_move[0]

def BoardFullCheck(board):
  if board.count(' ') >= 1:
    return False
  else:
   return True 

def main():
  print("Let's play some Tic-tac toe! You ready?")
  DisplayBoard()
  while not (BoardFullCheck(board)):
    if not isWinner(board,'O'):
      PlayersMove()
      if isWinner(board,'X'):
        print("Yayyy! You won! ^_^")
        break
      else:
        move = compMove()
        LetterInsert('O',move)
        print("Computer placed an 'O' in position", move,".")
      DisplayBoard()
    else:
      print("YOU LOST!!!!Computer beat you this time!!")
      break
  if BoardFullCheck(board):
    print("It's a TIE!")

main()