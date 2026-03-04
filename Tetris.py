import copy
import random


class Tetris:
    def __init__(self):
        self.board = [[0]*10 for _ in range(20)]#
        self.pieces_0 = {
            "I": [[0, 0, 0, 0],
                  [1, 1, 1, 1],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]],
            "J": [[1, 0, 0],
                  [1, 1, 1],
                  [0, 0, 0]],
            "L": [[0, 0, 1],
                  [1, 1, 1],
                  [0, 0, 0]],
            "O": [[1, 1],
                  [1, 1]],
            "S": [[0, 1, 1],
                  [1, 1, 0],
                  [0, 0, 0]],
            "T": [[0, 1, 0],
                  [1, 1, 1],
                  [0, 0, 0]],
            "Z": [[1, 1, 0],
                  [0, 1, 1],
                  [0, 0, 0]]
        }
        self.pieces_90 = {
            "I": [[0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0],
                  [0, 0, 1, 0]],
            "J": [[0, 1, 1],
                  [0, 1, 0],
                  [0, 1, 0]],
            "L": [[0, 1, 0],
                  [0, 1, 0],
                  [0, 1, 1]],
            "O": [[1, 1],
                  [1, 1]],
            "S": [[0, 1, 0],
                  [0, 1, 1],
                  [0, 0, 1]],
            "T": [[0, 1, 0],
                  [0, 1, 1],
                  [0, 1, 0]],
            "Z": [[0, 0, 1],
                  [0, 1, 1],
                  [0, 1, 0]]
        }
        self.pieces_180 = {
            "I": [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [1, 1, 1, 1],
                  [0, 0, 0, 0]],
            "J": [[0, 0, 0],
                  [1, 1, 1],
                  [0, 0, 1]],
            "L": [[0, 0, 0],
                  [1, 1, 1],
                  [1, 0, 0]],
            "O": [[1, 1],
                  [1, 1]],
            "S": [[0, 0, 0],
                  [0, 1, 1],
                  [1, 1, 0]],
            "T": [[0, 0, 0],
                  [1, 1, 1],
                  [0, 1, 0]],
            "Z": [[0, 0, 0],
                  [1, 1, 0],
                  [0, 1, 1]]
        }
        self.pieces_270 = {
            "I": [[0, 1, 0, 0],
                  [0, 1, 0, 0],
                  [0, 1, 0, 0],
                  [0, 1, 0, 0]],
            "J": [[0, 1, 0],
                  [0, 1, 0],
                  [1, 1, 0]],
            "L": [[1, 1, 0],
                  [0, 1, 0],
                  [0, 1, 0]],
            "O": [[1, 1],
                  [1, 1]],
            "S": [[1, 0, 0],
                  [1, 1, 0],
                  [0, 1, 0]],
            "T": [[0, 1, 0],
                  [1, 1, 0],
                  [0, 1, 0]],
            "Z": [[0, 1, 0],
                  [1, 1, 0],
                  [1, 0, 0]]
        }

        self.piece = self.randomNewPiece(None)
        self.piece_next = self.randomPieceType()
        self.piece_held = self.randomPieceType()
        self.canHold = True
        self.death_reason = None

        self.lines_cleared = 0
        self.score = 0



    def printboard(self, tboard = None):
        if tboard is None: tboard = self.board
        for row in tboard:
            line = ""
            for col in row:
                if col == 0:
                    line += '█'*2
                elif col == 1:
                    line += f"\033[31m█\033[0m"*2
                else:
                    line += f"\033[32m█\033[0m"*2
            print(line)

    def printboardOrg(self, tboard = None):
        if tboard is None: tboard = self.board
        print("Int: 0  1  2  3  4  5  6  7  8  9")
        for i, row in enumerate(tboard):
            i = f'{i} ' if i < 10 else f'{i}'
            print(f'{i}: {row}')
        print("Int: 0  1  2  3  4  5  6  7  8  9")




    def randomPieceType(self):
        return random.choice(list(self.pieces_0.keys()))

    def randomNewPiece(self, ptype):
        ptype = ptype if ptype is not None else self.randomPieceType()
        x = 5 - round(len(self.pieces_0[ptype][0])/2)
        return {
            'pos': [0, x],
            'type': ptype,
            'rot': 0
        }





    def getPieceArray(self):
        if self.piece['rot'] == 0:
            return self.pieces_0[self.piece['type']]
        elif self.piece['rot'] == 90:
            return self.pieces_90[self.piece['type']]
        elif self.piece['rot'] == 180:
            return self.pieces_180[self.piece['type']]
        elif self.piece['rot'] == 270:
            return self.pieces_270[self.piece['type']]
        return "WTF WIE"


    def tempPutOnBoard(self):
        tboard = copy.deepcopy(self.board)

        piece_array = self.getPieceArray()

        for rowint, row in enumerate(piece_array):
            for colint, col in enumerate(row):
                if col == 1: tboard[rowint + self.piece['pos'][0]][colint + self.piece['pos'][1]] = 2
        return tboard

    def putOnBoard(self):
        piece_array = self.getPieceArray()

        for rowint, row in enumerate(piece_array):
            for colint, col in enumerate(row):
                if col == 1: self.board[rowint + self.piece['pos'][0]][colint + self.piece['pos'][1]] = 1


    def checkWallCollision(self):
        for rowint, row in enumerate(self.getPieceArray()):
            for colint, col in enumerate(row):
                # FÜR JEDEN TEIL DES PIECES
                if col == 1:
                    if colint + self.piece['pos'][1] < 0: return True
                    if colint + self.piece['pos'][1] > 9: return True
        return False

    def checkOtherPieceAndFloorCollision(self):
        piece_array = self.getPieceArray()
        for rowint, row in enumerate(piece_array):
            for colint, col in enumerate(row):
                # FÜR JEDEN TEIL DES PIECES
                if col == 1:
                    if rowint + self.piece['pos'][0] > 19:
                        return True
                    # WENN POS IM BOARD VON DEM TEIL BELEGT
                    if self.board[rowint + self.piece['pos'][0]][colint + self.piece['pos'][1]] != 0:
                        return True

        return False

    def nextPiece(self):
        self.piece = self.randomNewPiece(self.piece_next)
        self.piece_next = self.randomPieceType()
        if self.checkOtherPieceAndFloorCollision():
            self.death_reason = 'high'

    def clearlines(self):
        lines_cleared_this = 0
        for rowint, row in enumerate(self.board):
            if row == [1]*10:
                self.board.pop(rowint)
                self.board.insert(0, [0]*10)
                self.lines_cleared += 1
                lines_cleared_this += 1
        if lines_cleared_this == 1: self.score += 100
        elif lines_cleared_this == 2: self.score += 300
        elif lines_cleared_this == 3: self.score += 500
        elif lines_cleared_this == 4: self.score += 800

    def gamestate(self):
        return {
            'board': self.board,
            'fullBoard': self.tempPutOnBoard(),
            'current': self.piece,
            'next': self.piece_next,
            'held': self.piece_held,
            'canHold': self.canHold,
            'cleared': self.lines_cleared,
            'score': self.score
        }

    def input(self, action):
            action_type = ""

            if action == 'A':
                self.piece['pos'][1] -= 1
                action_type = "move"
            if action == 'D':
                self.piece['pos'][1] += 1
                action_type = "move"


            if action == "Q":
                self.piece['rot'] -= 90
                if self.piece['rot'] == -90: self.piece['rot'] = 270
                action_type = "rotate"
            if action == "E":
                self.piece['rot'] += 90
                if self.piece['rot'] == 360: self.piece['rot'] = 0
                action_type = "rotate"

            if action == "W":
                if self.canHold:
                    piece_tmp = copy.deepcopy(self.piece)
                    self.piece = self.randomNewPiece(self.piece_held)
                    self.piece_held = piece_tmp['type']
                    action_type = "hold"
                    self.canHold = False
                else:
                    self.death_reason = "hold"
                    return


            if action == 'S':
                self.piece['pos'][0] += 1
                action_type = "down"

            if action == 'SS':
                while not self.checkOtherPieceAndFloorCollision():
                    self.piece['pos'][0] += 1
                action_type = "down"


            if self.checkWallCollision():
                self.death_reason = "wall"
                return

            if action_type == "move":
                if self.checkOtherPieceAndFloorCollision():
                    self.death_reason = 'move_in_block'
                    return
            if action_type == "rotate":
                if self.checkOtherPieceAndFloorCollision():
                    self.death_reason = 'rotate_in_block'
                    return

            if action_type == "down":
                if self.checkOtherPieceAndFloorCollision():
                    self.piece['pos'][0] -= 1
                    self.putOnBoard()

                    self.clearlines()
                    self.nextPiece()
                    self.canHold = True


