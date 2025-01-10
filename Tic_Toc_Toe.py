board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
player1 = input("enter your name:\n player1:")
player2 = input("player2:")
turns = 1
def display_board(board):
    print(f'''{board[0][0]}  |{board[0][1]}  |{board[0][2]}\n---+---+---\n{board[1][0]}  |{board[1][1]}  |{board[1][2]}\n---+---+---\n{board[2][0]}  |{board[2][1]}  |{board[2][2]}''')

def get_player_move(player, board):
    if player == player1:
        print(f"{player1}")
        cell = (input("row:"), input("col:"))
        row, col = cell
        while True:
            try:
                row = int(row)
                col = int(col)
                if 0 <= row <= 2 and 0 <= col <= 2 :
                    if board[row][col] == ' ':
                        board[row][col] = "X"
                        break
                    else:
                        print("this cell is already accupied. plaese try again.")
                        cell = input("row:"), input("col:")
                        row, col = cell
                        continue  
                else:
                    print("invalid input. please try again.")
                    cell = (input("row:"), input("col:"))
                    row, col = cell
                    continue
            except ValueError:
                print("invalid input. please try again.")
                cell = (input("row:"), input("col:"))
                row, col = cell
                continue
            
    else:
        if player == player2:
            print(f"{player2}")
            cell = (input("row:"), input("col:"))
            row, col = cell
            while True:
                try:
                    row = int(row)
                    col = int(col)
                    if 0 <= row <= 2 and 0 <= col <= 2 :
                        print(board[row][col])
                        if board[row][col] == ' ':
                            board[row][col] = "O"
                            break
                        else:
                            print("this cell is already accupied. plaese try again.")
                            cell = input("row:"), input("col:")
                            row, col = cell
                            continue  
                    else:
                        print("invalid input. please try again.")
                        cell = (input("row:"), input("col:"))
                        row, col = cell
                        continue
                except ValueError:
                    print("invalid input. please try again.")
                    cell = (input("row:"), input("col:"))
                    row, col = cell
                    continue
def check_win(board):
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                if row[0] == "X":
                    print(f"{player1} won!")
                else:
                    print(f"{player2} won!")
                return False
            
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                if row[0][col] == "X":
                    print(f"{player1} won!")
                else:
                    print(f"{player2} won!")
                return False
            
                
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            if board[0][0] == "X":
                print(f"{player1} won!")
            else:
                print(f"{player2} won!")
            return False
        
        elif board[0][2] == board[1][1] == board[2][0] != ' ':
            if board[0][2] == "X":
                print(f"{player1} won!")
            else:
                print(f"{player2} won!")
            return False
    
def draw(board):
    i=0
    while i < 3:
        for row in board:
            if row[0] != ' ' and row[1] != ' ' and  row[2] != ' ':
                i = i +1  
            else: 
                return None    
    else:
        print("draw")
        return False

while check_win(board) == None and draw(board) == None:
    if turns%2 != 0:
        get_player_move(player1, board)
        display_board(board)
        
    else:
        get_player_move(player2, board)
        display_board(board)
    
    turns =turns+1  
    
        

