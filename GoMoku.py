###############################################################################
#   Computer Project #11
#   Algorithm
#   Play the game, Gomoku.
#       Prompt for valid row and column inputs.
#       Output the board after every input.
#       Keep prompting until a winner is reached (5 in a row).
#           Once a winner is reached, print the winner of the game.
###############################################################################

class GoPiece(object):
    ''' 
    Represents the pieces used in the Gomoku game.
    '''
    def __init__(self, color="black"):
        '''
        Creates a Gomoku piece.
        color: The color of the game piece. defaults to black.
        '''
        # if the color is black, the piece is black.
        if color == "black":
            self.__color = "black"
        # if the color is white, the piece is white. 
        elif color =="white":
            self.__color = "white"
        # for any other color, there is an error.
        else:
            raise MyError("Wrong color.")
   
    def __str__(self):
        '''
        Displays the Game pieces.
        '''
        # if the color is black, return the black piece.
        if self.__color == "black":
            return  ' ● ' 
        # if the color is white, return the white peice.
        if self.__color == "white":
            return  ' ○ ' 
    
    def get_color(self):
        '''
        Returns the color of the piece as a string .
        '''
        return self.__color
            
class MyError(Exception):
    def __init__(self,value):
        self.__value = value
    def __str__(self):
        return self.__value

class Gomoku(object):
    '''
    Displays the game board and plays the game.
    '''
    
    def __init__(self,board_size=15,win_count=5,current_player="black"):
        ''' 
        Verifies incoming values & checks if they are in valid range.
        board_size: How big the board is. defaults to 15.
        win_count: How many pieces are needed for a win. Always at 5.
        current_player: the player with the turn. Defaults to black.
        '''
        # convert the size of the board and the wins to integers.
        try:
            valb = int(board_size)
            valw = int(win_count)
        # unless there's a value error.
        except ValueError:
            raise ValueError
        # if the size of the board is less than 0, raise a value error.
        if board_size <= 0:
            raise ValueError
        # if the player isn't black or white, raise an error.
        if current_player not in ["black","white"]:
            raise MyError("Wrong color.")
        
        # make the input values private.
        self.__board_size = board_size
        self.__win_count = win_count
        self.__current_player = current_player
        
        # create the game board.
        self.__go_board = [ [ ' - ' for j in range(self.__board_size)]\
                             for i in range(self.__board_size)]


    def assign_piece(self,piece,row,col):
        ''' 
        Places the piece at the specified position on the game board.
        piece: the piece placed on the game board(GoPiece object).
        row: the rows of the game board.
        col: the columns of the game board.
        '''
        # convert the row and columns into integers.
        try:
            valr = int(row)
            valc = int(col)
        # unless there is a ValueError.
        except ValueError:
            raise ValueError
        
        # check if row and col are within range
        if ((row >=1) and (row <= self.__board_size)):
            if ((col >=1) and (col <= self.__board_size)):
            
                # check if the position on the board is empty.
                if self.__go_board[row-1][col-1] == ' - ':
                    # if so, assign the piece on that position.
                    self.__go_board[row-1][col-1] = piece
                # if not, raise MyError.
                else:
                    raise MyError('Position is occupied.')
            # if the columns aren't in range, raise MyError.
            else:
                raise MyError('Invalid position.')
        # if the rows aren't in range, raise MyError.
        else:
            raise MyError('Invalid position.')
        

    def get_current_player(self):
        ''' return color of current player'''
        return self.__current_player
    

    
    def switch_current_player(self):
        ''' swicthes to other player '''
        # if the current player is black, siwtch to white.
        if self.__current_player == "black":
            self.__current_player = "white"
        # else, the current player is black.
        else:
            self.__current_player = "black"
            
        
    
    def __str__(self):
        s = '\n'
        for i,row in enumerate(self.__go_board):
            s += "{:>3d}|".format(i+1)
            for item in row:
                s += str(item)
            s += "\n"
        line = "___"*self.__board_size
        s += "    " + line + "\n"
        s += "    "
        for i in range(1,self.__board_size+1):
            s += "{:>3d}".format(i)
        s += "\n"
        s += 'Current player: ' + ('●' if self.__current_player == 'black' else '○')
        return s
        

    
    def current_player_is_winner(self):
        ''' 
        Returns True when there's a winner, otherwise False.
        '''
        # if the current player is black, black is the winning piece.
        if self.__current_player == "black":
            winnerPiece = GoPiece('black')
        # else, white wins.
        else:
            winnerPiece = GoPiece('white')
    
        # initialize a count for the winner   
        cur_count = 0
        
        # iterate through the rows.
        for i in range(self.__board_size):
            cur_count = 0
            for j in range(self.__board_size):
                #check if the consecutive pieces match the winner piece.
                if str(self.__go_board[i][j]) == str(winnerPiece):
                    # if so, add 1 to the count.
                    cur_count += 1
                   # else, reset it to 0.
                else:
                    cur_count = 0
                # if there are 5 in a row, there is a winner.
                if cur_count == 5:
                    return True
         
        # iterate through columns
        for j in range(self.__board_size):
            cur_count = 0
            for i in range(self.__board_size):
                # check if the consecutive pieces match the winner peice.
                if str(self.__go_board[i][j]) == str(winnerPiece):
                    # if so, add 1 to the count.
                    cur_count += 1
                    # else, reset it to 0.
                else:
                    cur_count = 0
                # if there are 5 pieces in a row, there's a winner.
                if cur_count == 5:
                    return True
                
        # iterate through left to right diagonally.       
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                # store the rows and columns into variables.
                r=i
                c=j
                cur_count = 0
                # loop thorugh the rows and columns, 
                while (r >= 0 and r < self.__board_size and\
                       c >=0 and c < self.__board_size):
                    # check if the consecutive pieces match the winner piece.
                    if str(self.__go_board[r][c]) == str(winnerPiece):
                        # if so, add 1 to the count
                        cur_count += 1
                        # else, reset it to 0.
                    else:
                        cur_count = 0
                    # if there are 5 pieces in a row, there's a winner.
                    if cur_count == 5:
                        return True
                    # shift between rows and columns.
                    r += 1
                    c += 1
                
        # iterate right to left diagonally.
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                r=i
                c=j
                
                while (r >= 0 and r < self.__board_size and\
                       c >=0 and c < self.__board_size ):
                    # check if the consecutive pieces match the winner piece.
                    if str(self.__go_board[r][c]) == str(winnerPiece):
                        # if so, add 1 to the count.
                        cur_count += 1
                    # else, reset it to 0.
                    else:
                        cur_count = 0
                        # if there are 5 pieces in a row, there's a winner.
                    if cur_count == 5:
                        return True
                    # shift between rows and columns.
                    r -= 1
                    c += 1        
        # if there aren't more than 5 pieces connected, return false.
        return False
    

def main():
    # call the board from the Gomoku class.
    board = Gomoku()
    # display the board.
    print(board)
    # prompt the players for a position to place a piece.
    play = input("Input a row then column separated by a comma (q to quit): ")
    while play.lower() != 'q':
        # split the inputs by the commas.
        play_list = play.strip().split(',')
        try: 
            # if there aren't two inputs, raise MyError.
            if len(play_list) != 2:
                raise MyError("Incorrect input.")
            
            # turn both the row and column input into an integer.
            r = int(play_list[0])
            c = int(play_list[1])
            
            # get color of the first player (Black).
            player_color = board.get_current_player()
            # get the piece of the first player(Black).
            
            p1 = GoPiece(player_color)
            # keep assigning pieces to the board.
            
            board.assign_piece(p1,r,c)
            # if there is a winner,
            
            if board.current_player_is_winner():
                # print the board.
                print(board)
                # print the winner of the game.
                print("{} Wins!".format(board.get_current_player()))
                break
            
            board.switch_current_player()
        except ValueError:
            # if there is a value error, print an error message and reprompt.
            print("Incorrect input.")
            print("Try again.")
            # If there is a MyError, reprompt.
        except MyError as error_message:
            print("{:s}\nTry again.".format(str(error_message)))
        print(board)
        play = input("Input a row then column separated by a comma (q to quit): ")


if __name__ == '__main__':
    main()
