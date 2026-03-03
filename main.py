import copy
import random

board = [[0]*10 for _ in range(20)]

def boom():
    print("""
                                 .               
                             .               
                             .       :       
                             :      .        
                    :..   :  : :  .          
                       ..  ; :: .            
                          ... .. :..         
                         ::: :...            
                     ::.:.:...;; .....       
                  :..     .;.. :;     ..     
                        . :. .  ;.           
                         .: ;;: ;.           
                        :; .BRRRV;           
                           YB BMMMBR         
                          ;BVIMMMMMt         
                    .=YRBBBMMMMMMMB          
                  =RMMMMMMMMMMMMMM;          
                ;BMMR=VMMMMMMMMMMMV.         
               tMMR::VMMMMMMMMMMMMMB:        
              tMMt ;BMMMMMMMMMMMMMMMB.       
             ;MMY ;MMMMMMMMMMMMMMMMMMV       
             XMB .BMMMMMMMMMMMMMMMMMMM:      
             BMI +MMMMMMMMMMMMMMMMMMMMi      
            .MM= XMMMMMMMMMMMMMMMMMMMMY      
             BMt YMMMMMMMMMMMMMMMMMMMMi      
             VMB +MMMMMMMMMMMMMMMMMMMM:      
             ;MM+ BMMMMMMMMMMMMMMMMMMR       
              tMBVBMMMMMMMMMMMMMMMMMB.       
               tMMMMMMMMMMMMMMMMMMMB:        
                ;BMMMMMMMMMMMMMMMMY          
                  +BMMMMMMMMMMMBY:           
                    :+YRBBBRVt; 
    """)
    quit()


pieces_0 = {
    "I":  [[0, 0, 0, 0],
           [1, 1, 1, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],
    "J":  [[1, 0, 0],
           [1, 1, 1],
           [0, 0, 0]],
    "L":  [[0, 0, 1],
           [1, 1, 1],
           [0, 0, 0]],
    "O":  [[1, 1],
           [1, 1]],
    "S":  [[0, 1, 1],
           [1, 1, 0],
           [0, 0, 0]],
    "T":  [[0, 1, 0],
           [1, 1, 1],
           [0, 0, 0]],
    "Z":  [[1, 1, 0],
           [0, 1, 1],
           [0, 0, 0]]
}
pieces_90 = {
    "I":  [[0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 1, 0],
           [0, 0, 1, 0]],
    "J":  [[0, 1, 1],
           [0, 1, 0],
           [0, 1, 0]],
    "L":  [[0, 1, 0],
           [0, 1, 0],
           [0, 1, 1]],
    "O":  [[1, 1],
           [1, 1]],
    "S":  [[0, 1, 0],
           [0, 1, 1],
           [0, 0, 1]],
    "T":  [[0, 1, 0],
           [0, 1, 1],
           [0, 1, 0]],
    "Z":  [[0, 0, 1],
           [0, 1, 1],
           [0, 1, 0]]
}
pieces_180 = {
    "I":  [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [1, 1, 1, 1],
           [0, 0, 0, 0]],
    "J":  [[0, 0, 0],
           [1, 1, 1],
           [0, 0, 1]],
    "L":  [[0, 0, 0],
           [1, 1, 1],
           [1, 0, 0]],
    "O":  [[1, 1],
           [1, 1]],
    "S":  [[0, 0, 0],
           [0, 1, 1],
           [1, 1, 0]],
    "T":  [[0, 0, 0],
           [1, 1, 1],
           [0, 1, 0]],
    "Z":  [[0, 0, 0],
           [1, 1, 0],
           [0, 1, 1]]
}
pieces_270 = {
    "I":  [[0, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 1, 0, 0],
           [0, 1, 0, 0]],
    "J":  [[0, 1, 0],
           [0, 1, 0],
           [1, 1, 0]],
    "L":  [[1, 1, 0],
           [0, 1, 0],
           [0, 1, 0]],
    "O":  [[1, 1],
           [1, 1]],
    "S":  [[1, 0, 0],
           [1, 1, 0],
           [0, 1, 0]],
    "T":  [[0, 1, 0],
           [1, 1, 0],
           [0, 1, 0]],
    "Z":  [[0, 1, 0],
           [1, 1, 0],
           [1, 0, 0]]
}

def printboard(tboard = None):
    if tboard is None: tboard = board
    for row in tboard:
        line = ""
        for col in row:
            line += f"\033[31m█\033[0m"*2 if col != 0 else '█'*2
        print(line)

def printboardOrg(tboard = None):
    if tboard is None: tboard = board
    print("Int: 0  1  2  3  4  5  6  7  8  9")
    for i, row in enumerate(tboard):
        i = f'{i} ' if i < 10 else f'{i}'
        print(f'{i}: {row}')
    print("Int: 0  1  2  3  4  5  6  7  8  9")




def randomPieceType():
    return random.choice(list(pieces_0.keys()))

def randomNewPiece(ptype):
    ptype = ptype if ptype is not None else randomPieceType()
    x = 5 - round(len(pieces_0[ptype][0])/2)
    return {
        'pos': [0, x],
        'type': ptype,
        'rot': 0
    }


piece = randomNewPiece(None)
piece_next = randomPieceType()
piece_held = randomPieceType()
canHold = True


def getPieceArray():
    if piece['rot'] == 0:
        return pieces_0[piece['type']]
    elif piece['rot'] == 90:
        return pieces_90[piece['type']]
    elif piece['rot'] == 180:
        return pieces_180[piece['type']]
    elif piece['rot'] == 270:
        return pieces_270[piece['type']]
    return "WTF WIE"


def tempPutOnBoard():
    tboard = copy.deepcopy(board)

    piece_array = getPieceArray()

    for rowint, row in enumerate(piece_array):
        for colint, col in enumerate(row):
            if col == 1: tboard[rowint + piece['pos'][0]][colint + piece['pos'][1]] = 2
    return tboard

def putOnBoard():
    piece_array = getPieceArray()

    for rowint, row in enumerate(piece_array):
        for colint, col in enumerate(row):
            if col == 1: board[rowint + piece['pos'][0]][colint + piece['pos'][1]] = 1


def checkWallCollision():
    for rowint, row in enumerate(getPieceArray()):
        for colint, col in enumerate(row):
            # FÜR JEDEN TEIL DES PIECES
            if col == 1:
                print()
                if colint + piece['pos'][1] < 0: return True
                if colint + piece['pos'][1] > 9: return True
    return False

def checkOtherPieceAndFloorCollision():
    piece_array = getPieceArray()
    for rowint, row in enumerate(piece_array):
        for colint, col in enumerate(row):
            # FÜR JEDEN TEIL DES PIECES
            if col == 1:
                if rowint + piece['pos'][0] > 19:
                    return True
                # WENN POS IM BOARD VON DEM TEIL BELEGT
                if board[rowint + piece['pos'][0]][colint + piece['pos'][1]] != 0:
                    return True

    return False

def nextPiece():
    global piece, piece_next
    piece = randomNewPiece(piece_next)
    piece_next = randomPieceType()

def clearlines():
    for rowint ,row in enumerate(board):
        if row == [1]*10:
            board.pop(rowint)
            board.insert(0, [0]*10)



while True:
    printboard(tempPutOnBoard())
    action = input(f"HELD: {piece_held} | NEXT: {piece_next} -> ").upper()
    action_type = ""

    if action == 'A':
        piece['pos'][1] -= 1
        action_type = "move"
    if action == 'D':
        piece['pos'][1] += 1
        action_type = "move"


    if action == "Q":
        piece['rot'] -= 90
        if piece['rot'] == -90: piece['rot'] = 270
        action_type = "rotate"
    if action == "E":
        piece['rot'] += 90
        if piece['rot'] == 360: piece['rot'] = 0
        action_type = "rotate"

    if action == "W":
        if canHold:
            piece_tmp = copy.deepcopy(piece)
            piece = randomNewPiece(piece_held)
            piece_held = piece_tmp['type']
            action_type = "hold"
            canHold = False
        else:
            print("Cannot hold")
            boom()


    if action == 'S':
        piece['pos'][0] += 1
        action_type = "down"

    if action == 'SS':
        while not checkOtherPieceAndFloorCollision():
            piece['pos'][0] += 1
        action_type = "down"


    if checkWallCollision():
        print("Collision with wall")
        boom()

    if action_type == "move":
        if checkOtherPieceAndFloorCollision():
            print("Moved into other block")
            boom()
    if action_type == "rotate":
        if checkOtherPieceAndFloorCollision():
            print("Rotated into other block")
            boom()

    if action_type == "down":
        if checkOtherPieceAndFloorCollision():
            piece['pos'][0] -= 1
            putOnBoard()
            nextPiece()
            canHold = True
            clearlines()