from __future__ import annotations

import random
import turtle as t
from collections import namedtuple


class DefaultConfig:
    PEN_COLOR = 'red'
    PEN_FILL_COLOR = 'red'
    PEN_SIZE = 2
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    BACKGROUND_COLOR = 'orange'
    TURTLE_SPEED = 10
    HIDE_TURTLE = False
    DELAY = 0

    _config_list = [
        'PEN_COLOR', 'PEN_FILL_COLOR', 'PEN_SIZE', 'SCREEN_WIDTH', 'SCREEN_HEIGHT',
        'BACKGROUND_COLOR', 'TURTLE_SPEED', 'HIDE_TURTLE', 'DELAY',
    ]


class TurtleConfig(DefaultConfig):

    def _set_config_from_class(self, config_class):
        data = self._collect_config_data_from_class(config_class)
        for key, value in data.items():
            setattr(self, key, value)

    def _collect_config_data_from_class(self, config_class):
        data = {}
        for attr in self._config_list:
            value = getattr(config_class, attr, None)
            if value:
                data[attr] = value
        return data


class CustomTurtle(TurtleConfig, t.Turtle):

    def __init__(self, *args, **kwargs):
        super(CustomTurtle, self).__init__(*args, **kwargs)
        self.window = t.Screen()
        self._setup_class()

    def draw_amogus(self):

        pen_size = 2
        pen_color = 'black'
        fill_color = 'red'
        self.setheading(90)

        self.pensize(pen_size)
        self.pencolor(pen_color)
        self.fillcolor(fill_color)

        right_top_coord, _ = self._draw_amogus_backpack()

        self._draw_amogus_body(right_top_coord)
        self._draw_amogus_glasses(
            (right_top_coord[0] + 50, right_top_coord[1])
        )

    def _draw_amogus_body(self, start_point: tuple):
        self.move_to(start_point)
        self.begin_fill()
        self.down()
        self.circle(-25, extent=180)
        self.forward(80)
        self.circle(-10, extent=180)
        self.forward(10)
        self.left(90)
        self.forward(10)
        self.left(90)
        self.forward(10)
        self.circle(-10, extent=189)
        self.goto(start_point)
        self.end_fill()

    def _draw_amogus_glasses(self, start_point: tuple):
        self.move_to(start_point)
        self.down()
        self.setheading(0)
        self.fillcolor('#aeaff5')
        self.begin_fill()
        self.circle(-10, extent=180)
        self.forward(10)
        self.circle(-10, extent=180)
        self.forward(10)
        self.end_fill()

    def _draw_amogus_backpack(self):

        right_top_angle: tuple
        left_bottom_angle: tuple

        self.begin_fill()
        self.down()
        self.setheading(90)
        self.forward(50)
        self.circle(-10, extent=90)
        self.forward(10)
        right_top_angle = self.pos()

        self.right(90)
        self.forward(70)
        left_bottom_angle = self.pos()

        self.right(90)
        self.forward(10)
        self.circle(-10, extent=90)

        self.end_fill()

        return right_top_angle, left_bottom_angle

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

        self.move_to(coordinates)
        self.down()

        self.begin_fill()
        for _ in range(5):
            self.forward(length)
            self.right(120)
            self.forward(length)
            self.right(-48)
        self.end_fill()

    def draw_background(self, length: int = 25, squares_amount: int = 25):
        self.down()
        self.pencolor(self.get_random_color())
        for i in range(squares_amount):
            length += 10
            self.left(5)
            for _ in range(4):
                self.forward(length)
                self.left(90)

    def move_to(self, coordinates):
        self.up()
        self.goto(coordinates)

    def get_random_coordinates(self) -> tuple[int, int]:
        """Случайная координата в пределах координатной сетки экрана."""

        x = random.randint(*self.coordinates.x)
        y = random.randint(*self.coordinates.y)
        return x, y

    @staticmethod
    def get_random_color():
        hex_chars = [
            'a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3', '4',
            '5', '6', '7', '8', '9',
        ]
        return '#' + ''.join([random.choice(hex_chars) for i in range(6)])

    @property
    def coordinates(self) -> namedtuple:
        """
        Возвращает именованный кортеж с полями ``x`` и ``y``.

        Содержит границы осей х и у исходя из размеров экрана, что задаются
        параметрами класса ``CustomScreen.SCREEN_WIDTH`` и ``CustomScreen.SCREEN HEIGHT``.
        К примеру, если экран имеет размер 640х480, то поля будут иметь следующие значения:
            x = (-320, 320),
            y = (-240, 240)

        :return: Возвращает именованный кортеж, поля которого содержат кортежи границ
            одноименных осей ``x`` и ``y``.
        """

        coord = namedtuple('Coordinates', ['x', 'y'])
        coord.x = self.x_coordinates
        coord.y = self.y_coordinates
        return coord

    @property
    def x_coordinates(self) -> tuple:
        """
        Возвращает кортеж, с границами экрана по оси ``x``.

        К примеру, если экран имеет ширину 640px, то кортеж будет
        иметь следующие значения:
            (-320, 320)
        """
        return -1 * self.screen_width // 2, self.screen_width // 2

    @property
    def y_coordinates(self):
        """
        Возвращает кортеж, с границами экрана по оси ``у``.

        К примеру, если экран имеет высоту 480px, то кортеж будет
        иметь следующие значения:
            (-240, 240)
        """
        return -1 * self.screen_height // 2, self.screen_height // 2

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
        self.speed(self.TURTLE_SPEED)
        self.hideturtle() if self.HIDE_TURTLE else self.showturtle()

        self.window.setup(
            self.SCREEN_WIDTH,
            self.SCREEN_HEIGHT,
        )
        self.window.bgcolor(self.BACKGROUND_COLOR)

        t.delay(self.DELAY)

