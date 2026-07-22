import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        x, y = self.position
        dx, dy = move

        new_position = (x + dx, y + dy)
        self.position = new_position
        self.path.append(new_position)

        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()
        # up, down, left, right
        self.moves = [
            (0, 1),  # up
            (0, -1),  # down
            (-1, 0),  # left
            (1, 0)  # right
        ]

    def level_up(self):
        # add diagonal moves
        self.moves.extend([
            (1, 1),  # up-right
            (1, -1),  # down-right
            (-1, 1),  # up-left
            (-1, -1)  # down-left
        ])