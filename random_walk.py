from random import choice


class RandomWalk:
    # Класс для генерирования случайных блужданий

    def __init__(self, num_points=5000):
        # инициализирует атрибуты блуждания
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        # Определение направления и длины перемещения
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        step = distance * direction
        return step

    def fill_walk(self):
        # вычисляет све точки блуждания
        # Шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_points:
            # Отклонение нулевых перемещений
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений x и y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

