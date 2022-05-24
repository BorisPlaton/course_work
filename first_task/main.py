import turtle as t

from first_task.config import CustomConfig
from first_task.utils import CustomTurtle

cursor = CustomTurtle()
cursor.set_config_from_class(CustomConfig)
cursor.draw_stars()

t.mainloop()
