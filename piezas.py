from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self,color) -> None:
        self.color = color
        self.moved = False
    @abstractmethod
    def is_valid_move(self, board, start, end) -> bool:
        pass
    def move(self):
        self.moved = True

#Peón
class Pawn(Piece):
    name = "pawn"
    def __init__(self,color) -> None:
        super().__init__(color)
        self.enpassantable = False
    def is_valid_move(self, board, start, end) -> bool:
        initial_x, initial_y = start
        final_x, final_y = end
        #Move One Forward
        if board.get_piece(end) == None:
            if self.color == "white":
                if initial_x == final_x - 1 and initial_y == final_y:
                    self.enpassantable = False
                    return True
            else:
                if initial_x == final_x + 1 and initial_y == final_y:
                    self.enpassantable = False
                    return True
        #Move Two Forward
        if not self.moved:
            if self.color == "white":
                if initial_x == final_x - 2 and initial_y == final_y and board.get_piece((final_x - 1,initial_y)) == None and board.get_piece(end) == None:
                    self.enpassantable = True
                    return True
            else:
                if initial_x == final_x + 2 and initial_y == final_y and board.get_piece((final_x + 1,initial_y)) == None and board.get_piece(end) == None:
                    self.enpassantable = True
                    return True
        #Capture Piece
        if self.color == "white":
            if initial_x == final_x - 1 and abs(initial_y - final_y) == 1 and board.get_piece(end) != None and board.get_piece(end).color != self.color:
                self.enpassantable = False
                return True
        else:
            if initial_x == final_x + 1 and abs(initial_y - final_y) == 1 and board.get_piece(end) != None and board.get_piece(end).color != self.color:
                self.enpassantable = False
                return True
        # En passant
        if board.get_piece(end) == None:
            side_piece = board.get_piece((initial_x,final_y))
            if side_piece != None and side_piece.name == "pawn" and side_piece.color != self.color and side_piece.enpassantable:
                if self.color == "white":
                    if initial_x == final_x - 1 and abs(initial_y - final_y) == 1:
                        return True
                else:
                    if initial_x == final_x + 1 and abs(initial_y - final_y) == 1:
                        return True
        return False

#Torre
class Rook(Piece):
    name = "rook"
    def __init__(self,color) -> None:
        super().__init__(color)
    def is_valid_move(self, board, start, end) -> bool:
        #Implementen ustedes
        pass

#Caballo
class Knight(Piece):
    name = "knight"
    def __init__(self,color) -> None:
        super().__init__(color)
    def is_valid_move(self, board, start, end) -> bool:
        #Check if valid destination
        if board.get_piece(end) == None or board.get_piece(end).color != self.color:
            initial_x, initial_y = start
            final_x, final_y = end
            #Check if L move
            if abs(initial_x - final_x) == 2 and abs(initial_y - final_y) == 1:
                return True
            elif abs(initial_x - final_x) == 1 and abs(initial_y - final_y) == 2:
                return True
        return False

#Alfil
class Bishop(Piece):
    name = "bishop"
    def __init__(self,color) -> None:
        super().__init__(color)
    def is_valid_move(self, board, start, end) -> bool:
        #Esta es la solución de Copilot que NO anda
        #Check if valid destination
        if board.get_piece(end) == None or board.get_piece(end).color != self.color:
            initial_x, initial_y = start
            final_x, final_y = end
            #Check if diagonal move
            if abs(initial_x - final_x) == abs(initial_y - final_y):
                #Check if path is clear
                for i in range(1,abs(initial_x - final_x)):
                    if board.get_piece((min(initial_x,final_x) + i,min(initial_y,final_y) + i)) != None:
                        return False
                return True
        return False

#Reina
class Queen(Piece):
    name = "queen"
    def __init__(self,color) -> None:
        super().__init__(color)
    def is_valid_move(self, board, start, end) -> bool:
        #Implemente ustedes
        pass

#Rey
class King(Piece):
    name = "king"
    def __init__(self,color) -> None:
        super().__init__(color)
    def is_valid_move(self, board, start, end) -> bool:
        #Check if valid destination
        if board.get_piece(end) == None or board.get_piece(end).color != self.color:
            initial_x, initial_y = start
            final_x, final_y = end
            if abs(initial_x - final_x) <= 1 and abs(initial_y - final_y) <= 1:
                return True
        return False
