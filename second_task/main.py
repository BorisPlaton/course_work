import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes


def update_first_func(frame, line, x):
    line.set_ydata(np.cos(2 * (x + frame)))
    return [line]


def customize_axis(axis: Axes):
    axis.grid()
    axis.set_xlim(-10, 10)
    axis.set_ylim(-10, 10)
    axis.set_xlabel("Ocь Х")
    axis.set_ylabel("Ocь Y")
    axis.legend(loc='upper left')


def func_2(x):
    return [2 * x - 4 for x in x]


# ------- Data for the task -------
fig, axes = plt.subplots(1, 2, dpi=80, facecolor='#f0f0f0', edgecolor='k')

x_1 = np.arange(-10, 10, 0.1)
x_2 = [i for i in range(-10, 10)]
x_3 = np.arange(-10, 10, 0.1)

function_1 = np.cos(2 * x_1)
function_2 = func_2
function_3 = lambda x: (np.array(x) * 2 - 4) + np.cos(2 * x)
# ------------------------------

# ------- Creating Axes -------
func_1, = axes[0].plot(
    x_1, function_1,
    label='f(x) = cos(2x)',
    color='#fcba03',
    linewidth=2,
)
axes[0].plot(
    x_2, function_2(x_2),
    label='f(x) = 2x - 4',
    color='#eb363f',
    linewidth=1,
    linestyle='--',
    marker='o',
    markerfacecolor='#9c171e',
    markersize=5,
)
axes[1].plot(
    x_3, function_3(x_3),
    label='f(x) = cos(2x) + 2x - 4',
    linestyle='-.'
)
# ------------------------------

# ------- Axes and Figure Customization-------
fig.canvas.manager.set_window_title('Завдання №2')

axes[0].set_title('Перші два графіки', fontsize=16)
axes[1].set_title('Сума графикiв', fontsize=16)
customize_axis(axes[0])
customize_axis(axes[1])
# ------------------------------

# ------- An First Axis Animation -------
animation = FuncAnimation(
    fig,
    func=update_first_func,
    frames=np.arange(0, 4 * np.pi, 0.1),
    fargs=(func_1, x_1),
    interval=30,
    blit=True,
    repeat=True,
)
# ------------------------------

plt.show()
