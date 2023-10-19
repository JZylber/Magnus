from piezas import Rook, Bishop, Queen, Pawn
from tablero import Board
import pytest

@pytest.fixture
def clean_board() -> Board:
    return Board(clear=True)

class TestRook:
    @staticmethod
    def test_rook_into_empty_tile_north(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        assert clean_board.move_piece((3,3),(0,3))[0]
    @staticmethod
    def test_rook_into_empty_tile_south(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        assert clean_board.move_piece((3,3),(7,3))[0]
    @staticmethod
    def test_rook_into_empty_tile_west(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        assert clean_board.move_piece((3,3),(3,0))[0]
    @staticmethod
    def test_rook_into_empty_tile_east(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        assert clean_board.move_piece((3,3),(3,7))[0]
    @staticmethod
    def test_rook_capture_piece_north(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((1,3),Pawn("black"))
        assert clean_board.move_piece((3,3),(1,3))[0]
    @staticmethod
    def test_rook_capture_piece_south(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((5,3),Pawn("black"))
        assert clean_board.move_piece((3,3),(5,3))[0]
    @staticmethod
    def test_rook_capture_piece_west(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((3,1),Pawn("black"))
        assert clean_board.move_piece((3,3),(3,1))[0]
    @staticmethod
    def test_rook_capture_piece_east(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((3,5),Pawn("black"))
        assert clean_board.move_piece((3,3),(3,5))[0]
    @staticmethod
    def test_rook_into_piece_north(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((1,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,3))[0]
    @staticmethod
    def test_rook_into_piece_south(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((5,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,3))[0]
    @staticmethod
    def test_rook_into_piece_west(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((3,1),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,1))[0]
    @staticmethod
    def test_rook_into_piece_east(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((3,5),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,5))[0]
    @staticmethod
    def test_rook_blocked_north(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((2,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,3))[0]
    @staticmethod
    def test_rook_blocked_south(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((4,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,3))[0]
    @staticmethod
    def test_rook_blocked_west(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((3,2),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,1))[0]
    @staticmethod
    def test_rook_blocked_east(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        clean_board.set_piece((3,4),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,5))[0]
    @staticmethod
    def test_rook_cannot_move_diagonally(clean_board):
        clean_board.set_piece((3,3),Rook("white"))
        assert not clean_board.move_piece((3,3),(5,5))[0]
        assert not clean_board.move_piece((3,3),(5,1))[0]
        assert not clean_board.move_piece((3,3),(1,1))[0]
        assert not clean_board.move_piece((3,3),(1,5))[0]
class TestBishop:
    @staticmethod
    def test_bishop_into_empty_tile_north_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        assert clean_board.move_piece((3,3),(0,0))[0]
    @staticmethod
    def test_bishop_into_empty_tile_north_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        assert clean_board.move_piece((3,3),(0,6))[0]
    @staticmethod
    def test_bishop_into_empty_tile_south_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        assert clean_board.move_piece((3,3),(6,0))[0]
    @staticmethod
    def test_bishop_into_empty_tile_south_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        assert clean_board.move_piece((3,3),(7,7))[0]
    @staticmethod
    def test_bishop_capture_piece_north_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((1,1),Pawn("black"))
        assert clean_board.move_piece((3,3),(1,1))[0]
    @staticmethod
    def test_bishop_capture_piece_north_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((1,5),Pawn("black"))
        assert clean_board.move_piece((3,3),(1,5))[0]
    @staticmethod
    def test_bishop_capture_piece_south_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((5,1),Pawn("black"))
        assert clean_board.move_piece((3,3),(5,1))[0]
    @staticmethod
    def test_bishop_capture_piece_south_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((5,5),Pawn("black"))
        assert clean_board.move_piece((3,3),(5,5))[0]
    @staticmethod
    def test_bishop_into_piece_north_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((1,1),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,1))[0]
    @staticmethod
    def test_bishop_into_piece_north_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((1,5),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,5))[0]
    @staticmethod
    def test_bishop_into_piece_south_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((5,1),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,1))[0]
    @staticmethod
    def test_bishop_into_piece_south_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((5,5),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,5))[0]
    @staticmethod
    def test_bishop_blocked_north_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((2,2),Pawn("white"))
        assert not clean_board.move_piece((3,3),(0,0))[0]
    @staticmethod
    def test_bishop_blocked_north_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((2,4),Pawn("white"))
        assert not clean_board.move_piece((3,3),(0,6))[0]
    @staticmethod
    def test_bishop_blocked_south_west(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((4,2),Pawn("white"))
        assert not clean_board.move_piece((3,3),(6,0))[0]
    @staticmethod
    def test_bishop_blocked_south_east(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        clean_board.set_piece((4,4),Pawn("white"))
        assert not clean_board.move_piece((3,3),(6,6))[0]
    @staticmethod
    def test_bishop_cannot_move_straight(clean_board):
        clean_board.set_piece((3,3),Bishop("white"))
        assert not clean_board.move_piece((3,3),(5,3))[0]
        assert not clean_board.move_piece((3,3),(1,3))[0]
        assert not clean_board.move_piece((3,3),(3,5))[0]
        assert not clean_board.move_piece((3,3),(3,1))[0]
class TestQueen:
    @staticmethod
    def test_queen_into_empty_tile_north(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(0,3))[0]
    @staticmethod
    def test_queen_into_empty_tile_south(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(7,3))[0]
    @staticmethod
    def test_queen_into_empty_tile_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(3,0))[0]
    @staticmethod
    def test_queen_into_empty_tile_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(3,7))[0]
    @staticmethod
    def test_queen_into_empty_tile_north_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(0,0))[0]
    @staticmethod
    def test_queen_into_empty_tile_north_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(0,6))[0]
    @staticmethod
    def test_queen_into_empty_tile_south_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(6,0))[0]
    @staticmethod
    def test_queen_into_empty_tile_south_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        assert clean_board.move_piece((3,3),(7,7))[0]
    @staticmethod
    def test_queen_capture_piece_north(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((1,3),Pawn("black"))
        assert clean_board.move_piece((3,3),(1,3))[0]
    @staticmethod
    def test_queen_capture_piece_south(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((5,3),Pawn("black"))
        assert clean_board.move_piece((3,3),(5,3))[0]
    @staticmethod
    def test_queen_capture_piece_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((3,1),Pawn("black"))
        assert clean_board.move_piece((3,3),(3,1))[0]
    @staticmethod
    def test_queen_capture_piece_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((3,5),Pawn("black"))
        assert clean_board.move_piece((3,3),(3,5))[0]
    @staticmethod
    def test_queen_capture_piece_north_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((1,1),Pawn("black"))
        assert clean_board.move_piece((3,3),(1,1))[0]
    @staticmethod
    def test_queen_capture_piece_north_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((1,5),Pawn("black"))
        assert clean_board.move_piece((3,3),(1,5))[0]
    @staticmethod
    def test_queen_capture_piece_south_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((5,1),Pawn("black"))
        assert clean_board.move_piece((3,3),(5,1))[0]
    @staticmethod
    def test_queen_capture_piece_south_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((5,5),Pawn("black"))
        assert clean_board.move_piece((3,3),(5,5))[0]
    @staticmethod
    def test_queen_into_piece_north(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((1,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,3))[0]
    @staticmethod
    def test_queen_into_piece_south(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((5,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,3))[0]
    @staticmethod
    def test_queen_into_piece_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((3,1),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,1))[0]
    @staticmethod
    def test_queen_into_piece_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((3,5),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,5))[0]
    @staticmethod
    def test_queen_into_piece_north_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((1,1),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,1))[0]
    @staticmethod
    def test_queen_into_piece_north_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((1,5),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,5))[0]
    @staticmethod
    def test_queen_into_piece_south_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((5,1),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,1))[0]
    @staticmethod
    def test_queen_into_piece_south_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((5,5),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,5))[0]
    @staticmethod
    def test_queen_blocked_north(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((2,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(1,3))[0]
    @staticmethod
    def test_queen_blocked_south(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((4,3),Pawn("white"))
        assert not clean_board.move_piece((3,3),(5,3))[0]
    @staticmethod
    def test_queen_blocked_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((3,2),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,1))[0]
    @staticmethod
    def test_queen_blocked_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((3,4),Pawn("white"))
        assert not clean_board.move_piece((3,3),(3,5))[0]
    @staticmethod
    def test_queen_blocked_north_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((2,2),Pawn("white"))
        assert not clean_board.move_piece((3,3),(0,0))[0]
    @staticmethod
    def test_queen_blocked_north_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((2,4),Pawn("white"))
        assert not clean_board.move_piece((3,3),(0,6))[0]
    @staticmethod
    def test_queen_blocked_south_west(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((4,2),Pawn("white"))
        assert not clean_board.move_piece((3,3),(6,0))[0]
    @staticmethod
    def test_queen_blocked_south_east(clean_board):
        clean_board.set_piece((3,3),Queen("white"))
        clean_board.set_piece((4,4),Pawn("white"))
        assert not clean_board.move_piece((3,3),(6,6))[0] 