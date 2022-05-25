import time
import turtle as t

from first_task.config import CustomConfig, SecondCustomConfig
from first_task.utils import CustomTurtle


def amogus_animation():
    cursor.move_to(
        (int(cursor.x_coordinates[0] + cursor.x_coordinates[0] * 0.1), 0)
    )

    k = 10
    flag = True
    screen.tracer(0)
    cursor.hideturtle()

    while True:
        time.sleep(1 / 60)

        if flag:
            k += 1
            if k == 30:
                flag = False
        else:
            k -= 1
            if k == 10:
                flag = True

        cursor.move_to(
            (int(cursor.x_coordinates[0] + cursor.x_coordinates[0] * 0.1), k)
        )
        screen.bgcolor(cursor.BACKGROUND_COLOR)
        cursor.draw_amogus()

        cursor.window.update()


cursor = CustomTurtle()
screen = t.Screen()
cursor.set_config_from_class(CustomConfig)

for _ in range(10):
    cursor.move_to(cursor.get_random_coordinates())
    cursor.draw_background(pattern_quantity=10)

cursor.set_config_from_class(CustomConfig)
cursor.draw_stars(length=10, stars_amount=10)
cursor.set_config_from_class(SecondCustomConfig)
cursor.draw_stars(length=10, stars_amount=15)

amogus_animation()
