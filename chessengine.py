class EstadoJogo():
    def __init__(self):
        self.tabuleiro = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.movimentoDasBrancas = True
        self.registroDeMovimentos = []

    def makeMovie(self, move):
        self.tabuleiro[move.startRow][move.startCol] = '--'
        self.tabuleiro[move.endRow][move.endCol] = move.pieceMoved
        self.registroDeMovimentos.append(move)
        self.movimentoDasBrancas = not self.movimentoDasBrancas

    def undoMovie(self):
        if len(self.registroDeMovimentos) != 0:
            self.tabuleiro[self.registroDeMovimentos[-1].startRow][self.registroDeMovimentos[-1].startCol] = self.registroDeMovimentos[-1].pieceMoved
            self.tabuleiro[self.registroDeMovimentos[-1].endRow][self.registroDeMovimentos[-1].endCol] = self.registroDeMovimentos[-1].pieceCaptured
            self.registroDeMovimentos.pop()
            self.movimentoDasBrancas = not self.movimentoDasBrancas
    
class Move():

    ranksToRows = {"1":7, "2":6, "3":5,"4":4,"5":3,"6":2,"7":1, '8':0}
    rowToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a":0, "b":1, "c":2,"d":3,"e":4,"f":5,"g":6, 'h':7}
    colsToFiles = {v:k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowToRanks[r]