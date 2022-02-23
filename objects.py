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
        return f"{self.floors} | {str(self.inside)} now at {str(self.now)} to {str(self.goal)}"

    def up(self):
        self.now += 1
        people_now = self.floors[self.now]  # позволяю тем, кто выйдет из лифта, сразу ехать дальше

        for index, man in enumerate(self.inside):
            if man.to_floor == self.now:
                print(man, 'came out')
                del self.inside[index]
                people_now.append(
                    Human(random.choice([k for k in range(0, len(self.floors) - 1) if k != self.now + 1])))

        if people_now:

            people_now.sort(key=lambda x: x.to_floor)
            to_del = list()
            for index, man in enumerate(people_now):

                if len(self.inside) == maximum:
                    break

                if man.to_floor > self.now:
                    print(man, 'came in')
                    self.inside += [man]
                    to_del += [man]
                    self.goal = max(man.to_floor, self.goal)

            for i in to_del:
                people_now.remove(i)

    def down(self):
        self.now -= 1
        people_now = self.floors[self.now]

        for index, man in enumerate(self.inside):
            if man.to_floor == self.now:
                print(man, 'came out')
                del self.inside[index]
                people_now.append(
                    Human(random.choice([k for k in range(0, len(self.floors) - 1) if k != self.now + 1])))

        if people_now:

            people_now.sort(key=lambda x: x.to_floor)
            to_del = list()
            for index, man in enumerate(people_now):

                if len(self.inside) == maximum:
                    break

                if man.to_floor < self.now:
                    print(man, 'came in')
                    self.inside += [man]
                    to_del += [man]
                    self.goal = min(man.to_floor, self.goal)

            for i in to_del:
                people_now.remove(i)
