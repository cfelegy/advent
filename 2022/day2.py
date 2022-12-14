from abc import ABC, abstractmethod

f = open('./inputs/day2_part1', 'r')
lines = f.readlines()
f.close()

# [A, B, C] -> Player1[Rock, Paper, Scissors]
# [X, Y, Z] -> Player2[Rock, Paper, Scissors]
# Score = Choice{Rock: 1, Paper: 2, Scissors: 3} + Outcome{Lose: 0, Draw: 3, Win: 6}

class GameObject(ABC):
    @abstractmethod
    def points() -> int: pass
    @abstractmethod
    def wins_against(): pass
    @abstractmethod
    def loses_against(): pass
    
    @staticmethod
    def from_text(text):
        if text in ['A', 'X']: return Rock()
        elif text in ['B', 'Y']: return Paper()
        else: return Scissors()

class Rock(GameObject):
    def points(self): return 1
    def wins_against(self): return Scissors
    def loses_against(self): return Paper

class Paper(GameObject):
    def points(self): return 2
    def wins_against(self): return Rock
    def loses_against(self): return Scissors

class Scissors(GameObject):
    def points(self): return 3
    def wins_against(self): return Paper
    def loses_against(self): return Rock

def play_game(me: GameObject, opponent: GameObject) -> int:
    if type(me) == type(opponent): return 3 + me.points()
    elif me.wins_against() == type(opponent): return 6 + me.points()
    else: return me.points()

part_1_points = 0

for line in lines:
    parts = line.strip().split(' ')
    opponent = GameObject.from_text(parts[0])
    me = GameObject.from_text(parts[1])
    part_1_points += play_game(me, opponent)

print('part1', part_1_points)

part_2_points = 0

for line in lines:
    parts = line.strip().split(' ')
    opponent = GameObject.from_text(parts[0])
    # lose
    if parts[1] == 'X':
        me = opponent.wins_against()()
        part_2_points += me.points()
    # draw
    elif parts[1] == 'Y':
        part_2_points += 3 + opponent.points()
    # win
    else:
        me = opponent.loses_against()()
        part_2_points += 6 + me.points()

print('part2', part_2_points)
