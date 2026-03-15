if __name__ == "__main__":
    class Tent:
        """
        Базовый класс, включающий в себя всевозможные палатки.

        Атрибуты:
            _name (str): название модели палатки (защищенный, чтобы избежать фальсификаций).
            _capacity (int): максимальное количество человек (защищенный, задаётся производителем при создании конкретной модели).
            _weight (float): вес палатки в кг (защищенный, задаётся производителем и не меняется с течением времени).
            _water_resistance (int): водонепроницаемость тента в мм водяного столба (защищенный, задаётся производителем после проведения испытаний).
        """

        def __init__(self, name: str, capacity: int, weight: float, water_resistance: int) -> None:
            """
            Инициализация базовой палатки.

            Аргументы:
                name: название модели.
                capacity: вместимость (количество человек).
                weight: вес (килограммы).
                water_resistance: водонепроницаемость (миллиметры водного столба).
            """
            self._name = name
            self._capacity = capacity
            self._weight = weight
            self._water_resistance = water_resistance

        def __str__(self) -> str:
            """Информация для покупателя"""
            return (f"Палатка {self._name}: вместимость {self._capacity} чел., вес {self._weight} кг, водонепроницаемость {self._water_resistance} мм")

        def __repr__(self) -> str:
            """Данные для разработчика"""
            return (f"Tent('{self._name}', {self._capacity}, {self._weight}, {self._water_resistance})")

        def get_info(self) -> dict:
            """
            Возвращает словарь с основными характеристиками палатки:
                dict: {'name': str, 'capacity': int, 'weight': float, 'water_resistance': int}
            """
            return {
                'name': self._name,
                'capacity': self._capacity,
                'weight': self._weight,
                'water_resistance': self._water_resistance
            }

        def set_weight(self, weight: float) -> None:
            """
            Устанавливает вес палатки с проверкой на знак числа.

            Аргументы:
                weight: новый вес (кг).

            Исключение:
                ValueError: если weight <= 0.
            """
            if weight <= 0:
                raise ValueError("Значение массы должно быть положительным числом")
            self._weight = weight

        def calculate_comfort(self) -> float:
            """
                На основе вместимости и массы палатки ассчитывает условный коэффициент комфорта палатки, чем больше коэффициент, тем  лучше.

                Возвращает:
                    float: коэффициент комфорта.
            """
            return self._capacity / (self._weight + 0.1)  # +0.1 чтобы избежать деления на ноль


    class TrekkingTent(Tent):
        """
        Класс трекинговой палатки, показывает наличие/отсутствие тамбура и объём заводской упаковки.
        """

        def __init__(self, name: str, capacity: int, weight: float, water_resistance: int, has_vestibule: bool, packed_volume: float) -> None:
            """
            Инициализация класса трекинговой палатки. Расширяем базовый класс, добавляя атрибуты для конкреиного типа палаток.

            Аргументы:
                name: название модели.
                capacity: вместимость (чел.)
                weight: вес (кг).
                water_resistance: водонепроницаемость (мм).
                has_vestibule: наличие тамбура.
                packed_volume: объём в упакованном виде (л).
            """
            super().__init__(name, capacity, weight, water_resistance)
            self._has_vestibule = has_vestibule  # защищенный, наличие или отсутствие тамбура постоянно
            self._packed_volume = packed_volume  # защищенный, объём ограничен транспортировочной упаковкой

        def __str__(self) -> str:
            """
            Перегруженная информация для покупателя.
            Добавляем информацию о наличии или отсутствии тамбура и объёме при транспортировке.
            """
            vestibule_str = "палатка с тамбуром" if self._has_vestibule else "тамбур не предусмотрен"
            return (f"Трекинговая палатка {self._name}: вместимость {self._capacity} чел., вес {self._weight} кг, водонепроницаемость {self._water_resistance} мм, {vestibule_str}, объём в упаковке {self._packed_volume} л")

        def __repr__(self) -> str:
            """
            Данные для разработчика, содержат все атрибуты трекинговой палатки.
            """
            return (f"TrekkingTent('{self._name}', {self._capacity}, {self._weight}, {self._water_resistance}, {self._has_vestibule}, {self._packed_volume})")

        def calculate_comfort(self) -> float:
            """
            Перегруженный метод расчёта коэффициента комфорта для трекинговой палатки.

            Причина перегрузки: у трекинговых палаток коэффициент комфорт зависит не только от вместимости и веса,
            но также от наличия тамбура и компактности при транспортировке. В расчёт добавляем выражения для корректировки баллов.

            Возвращает:
                float: пересчитанный коэффициент комфорта
            """
            base_comfort = super().calculate_comfort()
            # Начисляем баллы за тамбур и отнимаем за большой объём
            vestibule_bonus = 1.2 if self._has_vestibule else 1.0
            volume_penalty = 1.0 / (self._packed_volume + 0.1)  # чем меньше объём, тем лучше
            return base_comfort * vestibule_bonus * volume_penalty

        def get_packed_volume(self) -> float: # Унаследованный метод get_info() используется без изменений
            """
            Возвращает объём палатки в упаковке.

            Возвращает:
                float: объём в литрах.
            """
            return self._packed_volume

    # Write your solution here
    pass
