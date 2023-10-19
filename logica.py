from __future__ import annotations
from abc import ABC, abstractmethod
from tablero import Board
from jugador import Player

class GameState(ABC):
    def __init__(self,player:Player,oponent:Player,board:Board,screen_data) -> None:
        self.player = player
        self.oponent = oponent
        self.board = board
        self.screen_data = screen_data
    @abstractmethod
    def onClick(self,position) -> GameState:
        pass

class TurnStart(GameState):
    def __init__(self,player : Player,oponent: Player,board : Board, screen_data) -> None:
        screen_data["player_turn"] = player.color
        screen_data["selected_tile"] = None
        super().__init__(player,oponent,board,screen_data)
    def onClick(self,position) -> GameState:
        piece = self.board.get_piece(position)
        if piece and piece.color == self.player.color:
            return PieceSelected(self.player,self.oponent,position,self.board,self.screen_data)
        else:
            return self

class PieceSelected(GameState):
    def __init__(self,player : Player,oponent:Player,position, board : Board, screen_data) -> None:
        screen_data["selected_tile"] = position
        self.position = position
        super().__init__(player,oponent,board,screen_data)
    def onClick(self,destination) -> GameState:
        #captured_piece es None si no se capturo ninguna pieza
        valid_move,captured_piece = self.board.move_piece(self.position,destination)
        if valid_move:
            return TurnStart(self.oponent,self.player,self.board,self.screen_data)
        elif self.board.get_piece(destination) and self.board.get_piece(destination).color == self.player.color:
            return PieceSelected(self.player,self.oponent,destination,self.board,self.screen_data)
        else:
            return self

class GameEnd(GameState):
    def __init__(self,player : Player,oponent:Player,board : Board, screen_data) -> None:
        super().__init__(player,oponent,board,screen_data)
        screen_data["selected_tile"] = None
        if self.board.is_checkmate(self.oponent.color):
            screen_data["state"] = "checkmate"
        else:
            screen_data["state"] = "stalemate"
    def onClick(self,position) -> GameState:
        return self
