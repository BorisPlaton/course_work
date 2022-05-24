from __future__ import annotations

import random
import turtle as t
from collections import namedtuple

from first_task.config import DefaultConfig


class TurtleConfig:
    config = {
        'PEN_COLOR': None,
        'PEN_FILL_COLOR': None,
        'PEN_SIZE': None,
        'SCREEN_WIDTH': None,
        'SCREEN_HEIGHT': None,
        'BACKGROUND_COLOR': None,
    }

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._set_config_from_class(DefaultConfig)
        return obj

    def _set_config_from_class(self, config_class):
        data = self._collect_config_data_from_class(config_class)
        for key, value in data.items():
            setattr(self, key, value)

    def _collect_config_data_from_class(self, config_class):
        data = {}
        for attr in self.config:
            value = getattr(config_class, attr, None)
            if value:
                data[attr] = value
        return data


class CustomTurtle(TurtleConfig, t.Turtle):

    def __init__(self, *args, **kwargs):
        super(CustomTurtle, self).__init__(*args, **kwargs)
        self.window = t.Screen()
        self._setup_class()

    def draw_stars(self, length: int = 25, stars_amount: int = 5):
        """
        Рисует в случайных местах звезды с длиной ребра равной значению ``length``
        и общим количеством равным ``stars_amount``.

        :param length: Длина ребра звезды. По умолчанию 35.
        :param stars_amount: Количество звезд. По умолчанию 10.
        """

        for _ in range(stars_amount):
            self.left(random.randint(1, 360))
            self.draw_star(
                length,
                self.get_random_coordinates(),
            )

    def draw_star(self, length: int, coordinates: tuple):
        """
        Рисует звезду в точке ``coordinates`` с длиной ребра ``length``.

        :param length: Длина ребра звезды.
        :param coordinates: Координаты вида (x, y), в которых рисуют звезду.
        """

        self.penup()
        self.setposition(coordinates)
        self.pendown()

        self.begin_fill()
        for _ in range(5):
            self.forward(length)
            self.right(120)
            self.forward(length)
            self.right(-48)
        self.end_fill()

    def get_random_coordinates(self) -> tuple[int, int]:
        """Случайная координата в пределах координатной сетки экрана."""

        x = random.randint(*self.coordinates.x)
        y = random.randint(*self.coordinates.y)
        return x, y

    @property
    def coordinates(self) -> namedtuple:
        """
        Возвращает именованный кортеж с полями ``x`` и ``y``.

        Вычисляет границы осей х и у исходя из размеров экрана, что задаются
        параметрами класса ``CustomScreen.SCREEN_WIDTH`` и ``CustomScreen.SCREEN HEIGHT``.
        К примеру, если экран имеет размер 640х480, то поля будут иметь следующие значения:
            x = (-320, 320),
            y = (-240, 240)

        :return: Возвращает именованный кортеж, поля которого содержат кортежи границ
            одноименных осей ``x`` и ``y``.
        """

        coord = namedtuple('Coordinates', ['x', 'y'])
        coord.x = (-1 * self.screen_width // 2, self.screen_width // 2)
        coord.y = (-1 * self.screen_height // 2, self.screen_height // 2)
        return coord

    @property
    def screen_height(self):
        return self.screen.canvheight

    @property
    def screen_width(self):
        return self.screen.canvwidth

    def set_config_from_class(self, config_class):
        super(CustomTurtle, self)._set_config_from_class(config_class)
        self._setup_class()

    def _setup_class(self):
        self.pencolor(self.PEN_COLOR)
        self.fillcolor(self.PEN_FILL_COLOR)
        self.pensize(self.PEN_SIZE)

        self.window.setup(
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
        )
        self.window.bgcolor(self.BACKGROUND_COLOR)
