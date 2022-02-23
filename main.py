import random

from objects import *


class Game:
    def __init__(self):
        self.elevator = Elevator(random.randint(5, 20), 0, 0)
        self.floors_len = len(self.elevator.floors)

        for i in range(self.floors_len):
            self.elevator.floors[i] = [Human(random.choice([k for k in range(1, self.floors_len) if k != i + 1]))
                                       for j in range(random.randint(0, 5))]
        #what if 0 humans at the first floor?
        if len(self.elevator.floors[0]) == 0:
            self.elevator.floors[0] += [Human(self.floors_len)]
        self.step = 1
        self.elevator.goal = max([i.to_floor for i in self.elevator.floors[0]])
        self.elevator.inside = self.elevator.floors[0]
        self.elevator.floors[0] = []
        print(self.elevator)

    def play(self):
        self.elevator.up()
        print(self.elevator)



game = Game()
game.play()