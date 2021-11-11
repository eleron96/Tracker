class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f"Тип тренировки: {self.training_type}; "
                f"Длительность: {self.duration:.3f} ч.; "
                f"Дистанция: {self.distance:.3f} км; "
                f"Ср. скорость: {self.speed:.3f} км/ч; "
                f"Потрачено ккал: {self.calories:.3f}."
                )


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: int = 1000
    M_IN_HOUR: int = 60
    COEFF_CALORIE_1: float = 18
    COEFF_CALORIE_2: float = 20
    COEFF_CALORIE_3: float = 1.1
    COEFF_CALORIE_4: float = 2.0

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration_h = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration_h

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        return InfoMessage(
            self.__class__.__name__,
            self.duration_h,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP: float = 0.65

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_spent_calories(self) -> float:
        av_speed = self.get_mean_speed()
        return (((self.COEFF_CALORIE_1 * av_speed - self.COEFF_CALORIE_2)
                 * self.weight / self.M_IN_KM *
                 (self.duration_h * self.M_IN_HOUR)))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP: float = 0.65
    COEFF_CALORIE_SPORTSWALKING_1: float = 0.035
    COEFF_CALORIE_SPORTSWALKING_2: int = 2
    COEFF_CALORIE_SPORTSWALKING_3: float = 0.029

    def __init__(self,
                 action,
                 duration,
                 weight,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_spent_calories(self) -> float:
        return ((self.COEFF_CALORIE_SPORTSWALKING_1 * self.weight
                 + (self.get_mean_speed() ** self.COEFF_CALORIE_SPORTSWALKING_2
                    // self.height) * self.COEFF_CALORIE_SPORTSWALKING_3
                 * self.weight) * self.duration_h) * self.M_IN_HOUR


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38

    def __init__(self,
                 action,
                 duration,
                 weight,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool  # Длинна бассейна в метрах
        self.count_pool = count_pool  # Сколько раз проплыт бассейн

    def get_distance(self) -> float:
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return (((self.length_pool * self.count_pool)
                 / self.M_IN_KM) / self.duration_h)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.COEFF_CALORIE_3)
                * self.COEFF_CALORIE_4 * self.weight)


TRANING_TYPE_DICT = {
    'SWM': Swimming,
    'RUN': Running,
    'WLK': SportsWalking
}


def read_package(workout_type: str, data: list) -> Training:
    training_type = TRANING_TYPE_DICT[workout_type]
    return training_type(*data)


def main(training: Training) -> None:
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
