from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @abstractmethod
    def is_valid_entity(self):
        pass


class SnakeEntity(Entity):
    def __init__(self, start, end):
        super().__init__(start, end)

    def is_valid_entity(self):
        return self.start > self.end


class LadderEntity(Entity):
    def __init__(self, start, end):
        super().__init__(start, end)

    def is_valid_entity(self):
        return self.start < self.end
