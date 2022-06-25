import pytest

from bowling_game.bowling_game import Game


class TestBowlingGame:
    new_game: Game

    def set_up(self):
        self.new_game = Game()

    def roll_many(self, n: int, pins: int):
        for x in range(n):
            self.new_game.roll(pins)

    def test_new_game(self):
        self.set_up()
        self.roll_many(20, 0)
        assert self.new_game.score() == 0

    def test_all_ones(self):
        self.set_up()
        self.roll_many(20, 1)
        assert self.new_game.score() == 20

    def test_one_spare(self):
        self.set_up()

        self.new_game.roll(5)
        self.new_game.roll(5)  # spare
        self.new_game.roll(3)
        self.roll_many(17, 0)
        assert self.new_game.score() == 16


if __name__ == '__main__':
    pytest.main()
