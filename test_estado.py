from piezas import King, Pawn, Rook, Queen
from tablero import Board
from logica import TurnStart, PieceSelected, GameEnd
from jugador import Player
import pytest

@pytest.fixture
def clean_board() -> Board:
    return Board(clear=True)

@pytest.fixture
def start_game():
    board = Board()
    player1 = Player("white")
    player2 = Player("black")
    return TurnStart(player1,player2,board,{})

def test_start_game(start_game):
    assert start_game.player.color == "white"
    assert start_game.oponent.color == "black"

def test_piece_selected(start_game):
    new_state = start_game.onClick((1,0))
    assert isinstance(new_state,PieceSelected)
    assert new_state.player.color == "white"
    assert new_state.oponent.color == "black"
    assert new_state.position == (1,0)

def test_piece_selected_wrong_piece(start_game):
    new_state = start_game.onClick((2,0))
    assert isinstance(new_state,TurnStart)
    assert new_state.player.color == "white"
    assert new_state.oponent.color == "black"

def test_piece_selected_wrong_color(start_game):
    new_state = start_game.onClick((6,0))
    assert isinstance(new_state,TurnStart)
    assert new_state.player.color == "white"
    assert new_state.oponent.color == "black"

def test_piece_selected_move(start_game):
    new_state = start_game.onClick((1,0))
    new_state = new_state.onClick((3,0))
    assert isinstance(new_state,TurnStart)
    assert new_state.player.color == "black"
    assert new_state.oponent.color == "white"

def test_piece_selected_capture(clean_board):
    player1 = Player("white")
    player2 = Player("black")
    clean_board.set_piece((1,0),Pawn("white"))
    clean_board.set_piece((2,1),Pawn("black"))
    clean_board.set_piece((0,0),King("white"))
    clean_board.set_piece((7,7),King("black"))
    start_game = TurnStart(player1,player2,clean_board,{})
    new_state = start_game.onClick((1,0))
    new_state = new_state.onClick((2,1))
    assert isinstance(new_state,TurnStart)
    assert new_state.player.color == "black"
    assert new_state.oponent.color == "white"

def test_piece_selected_invalid_move(clean_board):
    player1 = Player("white")
    player2 = Player("black")
    clean_board.set_piece((1,0),Pawn("white"))
    clean_board.set_piece((2,1),Pawn("black"))
    clean_board.set_piece((0,0),King("white"))
    clean_board.set_piece((7,7),King("black"))
    start_game = TurnStart(player1,player2,clean_board,{})
    new_state = start_game.onClick((1,0))
    new_state = new_state.onClick((4,0))
    assert isinstance(new_state,PieceSelected)
    assert new_state.player.color == "white"
    assert new_state.oponent.color == "black"

def test_check(clean_board):
    player1 = Player("white")
    player2 = Player("black")
    clean_board.set_piece((0,0),King("white"))
    clean_board.set_piece((7,7),King("black"))
    clean_board.set_piece((6,5),Rook("white"))
    start_game = TurnStart(player1,player2,clean_board,{})
    new_state = start_game.onClick((6,5))
    new_state = new_state.onClick((7,5))
    assert isinstance(new_state,TurnStart)
    assert new_state.player.color == "black"
    assert new_state.oponent.color == "white"

def test_cannot_move_if_checked(clean_board):
    player1 = Player("white")
    player2 = Player("black")
    clean_board.set_piece((0,0),King("white"))
    clean_board.set_piece((7,7),King("black"))
    clean_board.set_piece((6,5),Rook("white"))
    start_game = TurnStart(player2,player1,clean_board,{})
    new_state = start_game.onClick((7,7))
    new_state = new_state.onClick((6,7))
    assert isinstance(new_state,PieceSelected)
    assert new_state.player.color == "black"
    assert new_state.oponent.color == "white"
    assert new_state.position == (7,7)
    assert new_state.board.get_piece((7,7)).name == "king"
    assert new_state.board.get_piece((6,7)) == None

def test_checkmate(clean_board):
    player1 = Player("white")
    player2 = Player("black")
    clean_board.set_piece((0,0),King("white"))
    clean_board.set_piece((7,7),King("black"))
    clean_board.set_piece((6,5),Rook("white"))
    clean_board.set_piece((5,4),Rook("white"))
    start_game = TurnStart(player1,player2,clean_board,{})
    new_state = start_game.onClick((5,4))
    new_state = new_state.onClick((7,4))
    assert isinstance(new_state,GameEnd)
    assert new_state.player.color == "white"
    assert new_state.oponent.color == "black"

def test_stalemate(clean_board):
    player1 = Player("white")
    player2 = Player("black")
    clean_board.set_piece((0,0),King("white"))
    clean_board.set_piece((7,0),King("black"))
    clean_board.set_piece((6,5),Queen("white"))
    start_game = TurnStart(player1,player2,clean_board,{})
    new_state = start_game.onClick((6,5))
    new_state = new_state.onClick((6,2))
    assert isinstance(new_state,GameEnd)
    assert new_state.player.color == "white"
    assert new_state.oponent.color == "black"
    assert not new_state.board.is_checkmate("black")
    assert new_state.board.is_stalemate("black")
    
    
