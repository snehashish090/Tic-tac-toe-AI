player, opponent = 'x', 'o'

# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def isMovesLeft(board) :

    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == " ") :
                return True
    return False

def evaluate(b) :

    # Checking for Rows for X or O victory.
    for row in range(3) :
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :
            if (b[row][0] == player) :
                return 10
            elif (b[row][0] == opponent) :
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3) :

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :

            if (b[0][col] == player) :
                return 10
            elif (b[0][col] == opponent) :
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :

        if (b[0][0] == player) :
            return 10
        elif (b[0][0] == opponent) :
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :

        if (b[0][2] == player) :
            return 10
        elif (b[0][2] == opponent) :
            return -10

    # Else if none of them have won then return 0
    return 0

# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax) :
    score = evaluate(board)

    # If Maximizer has won the game return his/her
    # evaluated score
    if (score == 10) :
        return score

    # If Minimizer has won the game return his/her
    # evaluated score
    if (score == -10) :
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if (isMovesLeft(board) == False) :
        return 0

    # If this maximizer's move
    if (isMax) :
        best = -1000

        # Traverse all cells
        for i in range(3) :
            for j in range(3) :

                # Check if cell is empty
                if (board[i][j]==" ") :

                    # Make the move
                    board[i][j] = player

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max( best, minimax(board,
                                              depth + 1,
                                              not isMax) )

                    # Undo the move
                    board[i][j] = " "
        return best

    # If this minimizer's move
    else :
        best = 1000

        # Traverse all cells
        for i in range(3) :
            for j in range(3) :

                # Check if cell is empty
                if (board[i][j] == " ") :

                    # Make the move
                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))

                    # Undo the move
                    board[i][j] = " "
        return best

# This will return the best possible move for the player
def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3) :
        for j in range(3) :

            # Check if cell is empty
            if (board[i][j] == " ") :

                # Make the move
                board[i][j] = player

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False)

                # Undo the move
                board[i][j] = " "

                # If the value of the current move is
                # more than the best value, then update
                # best/
                if (moveVal > bestVal) :
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove
# Driver code
board = [
    [ " ", " ", " " ],
    [ " ", " ", " " ],
    [ " ", " ", " " ]
]

def playMove(x, y, val):
    if board[x][y] == " ":
        board[x][y] = val

def printBoard(board):
    for i in board:
        print(i[0], "|", i[1], "|", i[2])

def checkDraw(board):
    empty = False
    for i in board:
        for j in i:
            if j == " ":
                empty = True
    if empty  == False:
        print("Draw!")
        exit()

def checkWin(board, player):
		ops = {
			(0,0):(2,2),
			(2,2):(0,0),
			(0,2):(2,0),
			(2,0):(0,2)

		}
		for i in board:
			if i[0] == player and i[1] == player and i[2] == player:
				printBoard(board)
				print('{} Wins!'.format(player))
				exit()
		for i in board[0]:
			index = board[0].index(i)
			if i == player and board[1][index] == player and board[2][index] == player:
				printBoard(board)
				print('{} Wins!'.format(player))
				exit()
		for i in ops:

			if board[i[0]][i[1]] == player and board[ops[i][0]][ops[i][1]] == player and board[1][1] == player:
				printBoard(board)
				print('{} Wins!'.format(player))
				exit()
print(
"""
/******************************************************/
Welcome to Tic Tac Toe AI by Snehashish Laskar (1538)
In this game you will play against an AI algorithm
To Play against this algorithm use the box numbers below

 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9

You will be prompted to play a move. Just type the box no.
/******************************************************/

"""
)

while True:
    printBoard(board)
    moves = {
        "1":(0,0),
        "2":(0,1),
        "3":(0,2),
        "4":(1,0),
        "5":(1,1),
        "6":(1,2),
        "7":(2,0),
        "8":(2,1),
        "9":(2,2),
    }
    move = input("Enter your move: ")
    for i in moves:
        if i in move:

            playMove(moves[i][0], moves[i][1], 'o')
            break
    bestMove = findBestMove(board)
    playMove(bestMove[0], bestMove[1], 'x')
    checkDraw(board)
    checkWin(board,'o')
    checkWin(board,'x')
