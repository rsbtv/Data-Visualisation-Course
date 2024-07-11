from random import randint


class Die:
    # Класс, представляющий один кубик

    def __init__(self, num_sides=6):
        # по умолчанию используется шестигранный кубик
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)