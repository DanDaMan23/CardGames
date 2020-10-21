class Chip:
    def __init__(self, color):
        chips = {"white": 1, "red": 5, "green": 25, "black": 100}
        self.color = color
        self._value = chips[color]

    @property
    def chip_value(self):
        return self._value

    def __repr__(self):
        return f"Color: {self.color} Value: {self.chip_value}"

class ChipPurchase:    
    @classmethod
    def add_chip(cls, color):
        return Chip(color)

    @classmethod
    def chip_set(cls, cash):
        chip_colors = [Chip("black"), Chip("green"), Chip("red"), Chip("white")]

        chips = []

        i = 0

        while cash != 0:
            if chip_colors[i].chip_value > cash:
                i += 1
            else:
                chips.append(chip_colors[i])
                cash -= chip_colors[i].chip_value

        return chips