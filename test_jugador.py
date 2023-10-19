from piezas import Rook, Bishop, Queen, Knight, Pawn, King
from jugador import Player
from logica import PieceSelected,TurnStart
from tablero import Board
import pytest

@pytest.fixture
def clean_board() -> Board:
    return Board(clear=True)

@pytest.fixture
def clean_board_w_kings() -> Board:
    board = Board(clear=True)
    board.set_piece((7,0),King("white"))
    board.set_piece((7,7),King("black"))
    return board

class TestPoints:
    @staticmethod
    def test_points_empty():
        player = Player("white")
        assert player.points() == 0
    @staticmethod
    def test_points_pawn():
        player = Player("white")
        player.capture_piece(Pawn("black"))
        assert player.points() == 1
    @staticmethod
    def test_points_knight():
        player = Player("white")
        player.capture_piece(Knight("black"))
        assert player.points() == 3
    @staticmethod
    def test_points_bishop():
        player = Player("white")
        player.capture_piece(Bishop("black"))
        assert player.points() == 3
    @staticmethod
    def test_points_rook():
        player = Player("white")
        player.capture_piece(Rook("black"))
        assert player.points() == 5
    @staticmethod
    def test_points_queen():
        player = Player("white")
        player.capture_piece(Queen("black"))
        assert player.points() == 9
    @staticmethod
    def test_points_multiple():
        player = Player("white")
        player.capture_piece(Pawn("black"))
        player.capture_piece(Knight("black"))
        player.capture_piece(Bishop("black"))
        player.capture_piece(Rook("black"))
        player.capture_piece(Queen("black"))
        assert player.points() == 21
class TestCapturedPieces:
    @staticmethod
    def test_captured_pieces():
        player = Player("white")
        pieces  = [Pawn("black"),Knight("black"),Bishop("black"),Rook("black"),Queen("black")]
        for piece in pieces:
            player.capture_piece(piece)
        captured_pieces = player.captured_pieces()
        for piece in captured_pieces:
            assert len(list(filter(lambda p: p.name == piece.name and p.color == piece.color,pieces))) == 1
class TestPieceCapture:
    @staticmethod
    def test_piece_capture_none(clean_board_w_kings:Board):
        white_player,black_player = Player("white"),Player("black")
        clean_board_w_kings.set_piece((0,0),Rook("white"))
        state = PieceSelected(white_player,black_player,(0,0),clean_board_w_kings,{})
        state = state.onClick((1,0))
        assert len(white_player.captured_pieces()) == 0
        assert len(black_player.captured_pieces()) == 0
        assert isinstance(state,TurnStart)
    @staticmethod
    def test_piece_capture(clean_board_w_kings:Board):
        white_player,black_player = Player("white"),Player("black")
        clean_board_w_kings.set_piece((0,0),Rook("white"))
        piece_to_capture = Pawn("black")
        clean_board_w_kings.set_piece((1,0),piece_to_capture)
        state = PieceSelected(white_player,black_player,(0,0),clean_board_w_kings,{})
        state = state.onClick((1,0))
        assert len(list(filter(lambda piece: piece.name == "pawn" and piece.color == "black", white_player.captured_pieces()))) == 1
        assert len(black_player.captured_pieces()) == 0
        assert isinstance(state,TurnStart)
    @staticmethod
    def test_change_selected_piece(clean_board_w_kings:Board):
        white_player,black_player = Player("white"),Player("black")
        clean_board_w_kings.set_piece((0,0),Rook("white"))
        clean_board_w_kings.set_piece((0,1),Knight("white"))
        clean_board_w_kings.set_piece((1,0),Pawn("black"))
        state = PieceSelected(white_player,black_player,(0,0),clean_board_w_kings,{})
        state = state.onClick((0,1))
        assert len(white_player.captured_pieces()) == 0
        assert len(black_player.captured_pieces()) == 0
        assert isinstance(state,PieceSelected)
    @staticmethod
    def test_invalid_capture(clean_board_w_kings:Board):
        white_player,black_player = Player("white"),Player("black")
        clean_board_w_kings.set_piece((0,0),Bishop("white"))
        clean_board_w_kings.set_piece((1,0),Pawn("black"))
        state = PieceSelected(white_player,black_player,(0,0),clean_board_w_kings,{})
        state = state.onClick((1,0))
        assert len(white_player.captured_pieces()) == 0
        assert len(black_player.captured_pieces()) == 0
        assert isinstance(state,PieceSelected)
    @staticmethod
    def test_invalid_movement(clean_board_w_kings:Board):
        white_player,black_player = Player("white"),Player("black")
        clean_board_w_kings.set_piece((0,0),Bishop("white"))
        state = PieceSelected(white_player,black_player,(0,0),clean_board_w_kings,{})
        state = state.onClick((2,0))
        assert len(white_player.captured_pieces()) == 0
        assert len(black_player.captured_pieces()) == 0
        assert isinstance(state,PieceSelected)