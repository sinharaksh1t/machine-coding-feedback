from board import Board
from entity import Entity, SnakeEntity, LadderEntity
from player import Player
from dice import Dice

if __name__ == "__main__":
    entity_list: list[Entity] = []
    player_list: list[Player] = []
    with open("input.txt", "r", encoding="utf-8") as f:
        s = int(f.readline())
        for _ in range(s):
            head, tail = f.readline().split()
            entity_list.append(SnakeEntity(int(head), int(tail)))

        l = int(f.readline())
        for _ in range(l):
            bottom, top = f.readline().split()
            entity_list.append(LadderEntity(int(bottom), int(top)))

        p = int(f.readline())
        for i in range(p):
            player_list.append(Player(f.readline().strip()))

    die: Dice = Dice(12)
    end = 200
    board = Board(player_list, entity_list, die, end)

    # Main game loop
    while True:
        who, from_pos, to_pos, roll = board.move_player()
        print(f"{who.name} rolled a {roll} and moved from {from_pos} to {to_pos}")
        if to_pos == end:
            print(f"{who.name} wins the game")
            break
        board.change_turn()
