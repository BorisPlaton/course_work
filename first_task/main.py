import turtle as t

from first_task.config import CustomConfig, SecondCustomConfig
from first_task.utils import CustomTurtle

cursor = CustomTurtle()

for _ in range(5):
    cursor.move_to(cursor.get_random_coordinates())
    cursor.draw_background()

cursor.set_config_from_class(CustomConfig)
cursor.draw_stars(length=10, stars_amount=10)

cursor.draw_amogus()

cursor.set_config_from_class(SecondCustomConfig)
cursor.draw_stars(length=10, stars_amount=15)

t.mainloop()
