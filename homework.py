class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


# Константы:

LEN_STEP: float = [1.38, 0.65]
M_IN_KM: int = 1000
coeff_calorie_1: float = 18
coeff_calorie_2: float = 20


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        pass

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        pass

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        # return InfoMessage(self.__class__.__name__,
        #                    self.duration,
        #                    self.get_distance(),
        #                    self.get_mean_speed(),
        #                    self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        av_speed = self.get_mean_speed()
        return (((coeff_calorie_1 * av_speed - coeff_calorie_2)
                 * self.weight) / (M_IN_KM * self.duration))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    self.height = height


class Swimming(Training):
    """Тренировка: плавание."""

    def __init__(self,
                 action,
                 duration,
                 weight,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_distance(self) -> float:
        return (self.length_pool * self.count_pool) / M_IN_KM

    def get_mean_speed(self) -> float:
        return ((self.length_pool * self.count_pool)
                / M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + coeff_calorie_1)
                * coeff_calorie_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
