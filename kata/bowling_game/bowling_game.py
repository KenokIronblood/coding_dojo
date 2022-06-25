class Game:
    #slide 39
    rolls: [int] = [0] * 21
    current_roll: int = 0

    def roll(self, pins: int) -> None:
        self.current_roll += 1
        self.rolls[self.current_roll] = pins

    def score(self) -> int:
        game_score: int = 0
        for roll in self.rolls:
            game_score += roll
        return game_score
