# Write your code here :-)
def chessValid(dictionary):
    valid = True
    whitePieces = 0
    blackPieces = 0
    pawnNumber = 0
    spaceList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pieceList = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    #too lazy to write out king count, but basically pawnNumber but checks kings

    for space, piece in dictionary.items():
        if piece[0] != 'w' and if piece[0] != 'b':
            valid = False
        if len(space) > 2:
            valid = False
        if space[0] == 0 or if space[0] == 9:
            valid = False
        if space[1] not in spaceList:
            valid = False
        if piece[1:] not in pieceList:
            valid = False


        if piece[0] == 'b':
            blackPieces += 1

        if piece[0] == 'w':
            whitePieces += 1

        if piece[1:] == 'pawn':
            pawnNumber += 1


    if whitePieces > 16 or if blackPieces > 16:
        valid = False
    if pawnNumber > 8:
        valid = False


    if valid == False:
        print('not a real board')
    else:
        print('real board')
