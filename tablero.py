from piezas import Piece, Rook, Knight, Bishop, Queen, King, Pawn

class Board:
    def __init__(self,clear = False):
        self.board = []
        if not clear:
            #White pieces
            self.board.append([Rook("white"), Knight("white"), Bishop("white"), Queen("white"), King("white"), Bishop("white"), Knight("white"), Rook("white")])
            self.board.append([Pawn("white") for _ in range(8)])
            for _ in range(4):
                self.board.append([None for _ in range(8)])
            #Black pieces
            self.board.append([Pawn("black") for _ in range(8)])
            self.board.append([Rook("black"), Knight("black"), Bishop("black"), Queen("black"), King("black"), Bishop("black"), Knight("black"), Rook("black")])
        else:
            for _ in range(8):
                self.board.append([None for _ in range(8)])
    
    def get_piece(self,position) -> Piece | None:
        return self.board[position[0]][position[1]]
    
    def set_piece(self,position,piece) -> None:
        self.board[position[0]][position[1]] = piece

    def move_piece(self,position1,position2) -> tuple[bool,Piece | None]:
        piece = self.get_piece(position1)
        if not piece:
            return False,None
        if piece.is_valid_move(self,position1,position2):
            captured_piece = self.get_piece(position2)
            piece.move()
            self.set_piece(position2,piece)
            self.set_piece(position1,None)
            return True, captured_piece
        return False,None
    def __str__(self) -> str:
        string = ""
        for row in self.board:
            for piece in row:
                if piece:
                    string += piece.color[0] + piece.name[0] + " "
                else:
                    string += "   "
            string += "\n"
        return string