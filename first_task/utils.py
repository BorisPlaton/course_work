from __future__ import annotations
import turtle as t


class CustomTurtle(t.Turtle):
    PEN_COLOR = '#cc3d4e'
    PEN_FILL_COLOR = '#cc3d4e'
    PEN_SIZE = 2

    def __init__(self, *args, **kwargs):
        super(CustomTurtle, self).__init__(*args, **kwargs)
        self._configure_turtle()

    def draw_stars(self, length: int = 100, stars_amount: int = 10):
        """
        Рисует звезды с длиной ребра ``length``  и
        количеством ``stars_amount``.

        :param length:
        :param stars_amount:
        """
        for _ in range(stars_amount):
            self._draw_star(length)

    def _draw_star(self, length):
        """
        Рисует звезду.

        :param length: Длина ребра звезды.
        """

        for _ in range(5):
            self.left(135)
            self.forward(length)

    def _configure_turtle(self):
        """
        Устанавливает стандартные настройки, что указанны в атрибутах класса.
        """

        self.pencolor(self.PEN_COLOR)
        self.fillcolor(self.PEN_FILL_COLOR)
        self.pensize(self.PEN_SIZE)


class CustomScreen:

    def __init__(self):
        self.screen = t.Screen()
        self.screen.exitonclick()
