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
        return (f"Тип тренировки: {self.training_type};"
                f"Длительность: {self.duration:.3f} ч.;"
                f"Дистанция: {self.distance:.3f} км.;"
                f"Ср. скорость: {self.speed:.3f} км/ч;"
                f"Потрачено ккал: {self.calories:.3f} .")


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = [1.38, 0.65]
    M_IN_KM: int = 1000
    coeff_calorie_1: float = 18
    coeff_calorie_2: float = 20

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
        return self.action * self.LEN_STEP[1] / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            self.training_type,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self) -> float:
        av_speed = self.get_mean_speed()
        return (((self.coeff_calorie_1 * av_speed - self.coeff_calorie_2)
                 * self.weight) / (self.M_IN_KM * self.duration))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calorie_SportsWalking_1: float = 0.035
    coeff_calorie_SportsWalking_2: int = 2
    coeff_calorie_SportsWalking_3: float = 0.029
    height: float = 180

    def get_spent_calories(self) -> float:
        return ((self.coeff_calorie_SportsWalking_1 * self.weight
                 + (self.get_mean_speed() ** self.coeff_calorie_SportsWalking_2
                    // self.height) * self.coeff_calorie_SportsWalking_3
                 * self.weight) * self.duration)


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
        return (self.length_pool * self.count_pool) / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return ((self.length_pool * self.count_pool)
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.coeff_calorie_1)
                * self.coeff_calorie_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        return Swimming(data[0], data[1], data[2], data[3], data[4])
    if workout_type == 'RUN':
        return Running(data[0], data[1], data[2])
    if workout_type == 'WLK':
        return SportsWalking(data[0], data[1], data[2])


def main(training: Training) -> None:
    """Главная функция."""
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
