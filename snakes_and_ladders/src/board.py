from player import Player
from entity import Entity
from dice import Dice


class Board:
    def __init__(self, players: list[Player], entities: list[Entity], dice: Dice, end: int = 100, ):
        self.start = 1
        self.end = end
        self.players = players
        self.turn = 0  # Player at 0th index always starts first
        self.entities: dict[int, Entity] = {}
        self.dice = dice
        self._construct_entity_map(entities)
        self._validate_board()

    def _construct_entity_map(self, entities: list[Entity]):
        for entity in entities:
            if entity.start in self.entities:
                raise ValueError("Board is invalid, two entities cannot start at the same position")
            self.entities[entity.start] = entity

    def _validate_board(self):
        # Ensure all entities are valid
        for entity in self.entities.values():
            if (entity.start not in range(self.start, self.end + 1)
                    or entity.end not in range(self.start, self.end + 1)
                    or not entity.is_valid_entity()):
                raise ValueError("Board is invalid, entities are not valid")

        # Check for cycle among entities
        for entity in self.entities.values():
            seen = set()
            while entity.end in self.entities:
                if entity.end in seen:
                    raise ValueError("Board is invalid, cycle detected")
                seen.add(entity.end)
                entity = self.entities[entity.end]

    def move_player(self) -> tuple[Player, int, int, int]:
        curr_player = self.players[self.turn]
        rolled = self.dice.roll_dice()
        curr_pos = curr_player.pos
        new_pos = curr_pos + rolled
        if not self._is_valid_move(new_pos):
            return curr_player, curr_pos, curr_pos, rolled

        while new_pos in self.entities:
            new_pos = self.entities[new_pos].end

        curr_player.pos = new_pos
        return curr_player, curr_pos, new_pos, rolled

    def _is_valid_move(self, new_pos: int):
        return new_pos in range(self.start, self.end + 1)

    def change_turn(self):
        self.turn = (self.turn + 1) % len(self.players)
