def makeBoardList(boardSize):
    boardList = []
    for x in range(boardSize):
        boardList.append([])
        for y in range(boardSize):
            boardList[x].append(" ")
    return boardList
def buildBoard(boardList):
    result = ["   "]
    for x in range(len(boardList)):
        result[0] += f" {x+1}  "
        row1 = f"{x+1} |"
        row2 = "  -"
        for y in range(len(boardList[x])):
            row1 += f" {boardList[x][y]} |"
            row2 += "----"
        result.append(row1)
        result.append(row2)
    return "\n".join(result)
def move(boardList,row,column,player):
    wrongMove = True
    try:
        if boardList[row - 1][column - 1] == " ":
            boardList[row - 1][column - 1] = player
            wrongMove = False
    except:
        pass
    return boardList,wrongMove
def winCondition(boardList,boardSize,player):
    scoreRightDiagonal = 0
    scoreLeftDiagonal = 0
    for x in range(boardSize):
        scoreHorizontal = 0
        scoreVertical = 0
        for y in range(boardSize):
            if boardList[x][y] == player:
                scoreHorizontal += 1
            if boardList[y][x] == player:
                scoreVertical += 1
        if boardList[x][x] == player:
            scoreRightDiagonal += 1
        if boardList[boardSize-x-1][x] == player:
            scoreLeftDiagonal += 1
        if scoreHorizontal == boardSize or scoreVertical == boardSize or scoreRightDiagonal == boardSize or scoreLeftDiagonal == boardSize:
            return True
    return False
def main():
    boardSize = int(input("Velkommen til x på rad! x = "))
    board = makeBoardList(boardSize)
    playerX = input("Hvem spiller X? ")
    playerO = input("Hvem spiller O? ")
    playerName = {"X":playerX,"O":playerO}
    player = "X"
    while True:
        for a in playerName:
            if winCondition(board, boardSize, a):
                print(f"{playerName[a]} vinner!")
                return
        row = int(input(f"{playerName[player]}, velg rad: "))
        column = int(input("Velg kolonne: "))
        board,wrongMove = move(board,row,column,player)
        if wrongMove:
            print("Ugyldig trekk!")
            continue
        else:
            print(buildBoard(board))
            if player == "O":
                player = "X"
            else:
                player = "O"
main()