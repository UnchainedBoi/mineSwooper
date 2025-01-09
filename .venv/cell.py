class Cell:
    def __init__(self):
        self.revealed = False
        self.flagged = False

    def to_string(self):
        raise NotImplementedError

class Mine(Cell):

    def to_string(self, reveal=False) -> str:
        if self.flagged and not reveal:
            return "F"
        if not self.revealed and not reveal:
            return "#"
        return "X"


class Number(Cell):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def to_string(self, reveal=False) -> str:
        if self.flagged and not reveal:
            return "F"
        if not self.revealed and not reveal:
            return "#"
        return str(self.value)