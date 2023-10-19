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
            self.board.append([Rook("black"), Knight("black"), Bishop("black"), Queen("black"),King("black"), Bishop("black"), Knight("black"), Rook("black")])
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
            return False, None
        if not piece.is_valid_move(self,position1,position2):
            return False, None
        captured_piece = self.get_piece(position2)
        # Check if en passant
        if piece.name == "pawn" and abs(position1[0] - position2[0]) == 1 and abs(position1[1] - position2[1]) == 1 and captured_piece == None:
            captured_piece = self.get_piece((position1[0],position2[1]))
            self.set_piece((position1[0],position2[1]),None)
        piece.move()
        self.set_piece(position2,piece)
        self.set_piece(position1,None)
        # Make other player pawns unenpassantable
        for i in range(8):
            for j in range(8):
                other_piece = self.get_piece((i,j))
                if other_piece and other_piece != piece and other_piece.name == "pawn" and other_piece.color == piece.color and other_piece.enpassantable:
                    other_piece.enpassantable = False
        return True, captured_piece
    
    def revert_move(self,position1,position2,captured_piece) -> None:
        piece = self.get_piece(position2)
        self.set_piece(position1,piece)
        self.set_piece(position2,captured_piece)
    
    def is_checked(self, color: str) -> bool:
        assert color in ["white","black"], "Invalid color"
        king_position = None
        for i in range(8):
            for j in range(8):
                piece = self.get_piece((i,j))
                if piece and piece.name == "king" and piece.color == color:
                    king_position = (i,j)
                    break
        assert king_position, "King not found"
        for i in range(8):
            for j in range(8):
                piece = self.get_piece((i,j))
                if piece and piece.color != color and piece.is_valid_move(self,(i,j),king_position):
                    return True
        return False
    
    def is_checkmate(self, color: str) -> bool:
        assert color in ["white","black"], "Invalid color"
        if not self.is_checked(color):
            return False
        for i in range(8):
            for j in range(8):
                piece = self.get_piece((i,j))
                if piece and piece.color == color:
                    for k in range(8):
                        for l in range(8):
                            valid,captured_piece = self.move_piece((i,j),(k,l))
                            if valid:
                                if not self.is_checked(color):
                                    self.revert_move((i,j),(k,l),captured_piece)
                                    return False
                                self.revert_move((i,j),(k,l),captured_piece)
        return True

    def is_stalemate(self, color: str) -> bool:
        assert color in ["white","black"], "Invalid color"
        if self.is_checked(color):
            return False
        for i in range(8):
            for j in range(8):
                piece = self.get_piece((i,j))
                if piece and piece.color == color:
                    for k in range(8):
                        for l in range(8):
                            valid,captured_piece = self.move_piece((i,j),(k,l))
                            if valid:
                                if not self.is_checked(color):
                                    self.revert_move((i,j),(k,l),captured_piece)
                                    return False
                                self.revert_move((i,j),(k,l),captured_piece)
        return True

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