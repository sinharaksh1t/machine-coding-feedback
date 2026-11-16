class Player:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Player name is required")
        self.name = name
        self.pos = 0
