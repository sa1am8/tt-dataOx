import random

maximum = 5

class Human:
    def __init__(self, to_floor: int):
        self.to_floor = to_floor

    def __repr__(self):
        return str(self.to_floor)




class Elevator:
    def __init__(self, floors: list, goal: int, inside: list, now=0):
        self.floors = [[] for i in range(floors)]
        self.goal = goal
        self.inside = inside
        self.now = now

    def __repr__(self):
        return f"{self.floors} | {str(self.inside)} to {str(self.goal)}"

    def up(self):
        self.now += 1
        people_now = self.floors[self.now] # позволяю тем, кто выйдет из лифта, сразу ехать дальше

        for index, man in enumerate(self.inside):
            if man.to_floor == self.now:
                print(man, 'came out')
                people_now.append(man)
                del self.inside[index]
                people_now.append(Human(random.choice([k for k in range(1, self.floors_len) if k != self.now + 1])))

        if people_now:
            if len(self.inside) == maximum:
                return
            people_now.sort()
            for index, man in enumerate(people_now):
                if man.to_floor < self.goal:
                    print(man, 'came in')
                    self.inside += [man]
                    del people_now[index]
