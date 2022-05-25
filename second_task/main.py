import time

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def customize_first_figure(axis: Axes):
    axis.grid()
    axis.set_xlim(-10, 10)
    axis.set_ylim(-10, 10)
    axis.set_title("Перші два графіки", fontsize=16)
    axis.set_xlabel("Ocь Х")
    axis.set_ylabel("Ocь Y")
    axis.legend(loc='upper left')


def customize_second_figure(axis: Axes):
    axis.grid()
    axis.set_xlim(-10, 10)
    axis.set_ylim(-10, 10)
    axis.set_title("Сума двох графикiв", fontsize=16)
    axis.set_xlabel("Ocь Х")
    axis.set_ylabel("Ocь Y")
    axis.legend(loc='upper left')


def func_2(x):
    return [2 * i for i in x]


fx, axes = plt.subplots(1, 2, dpi=80, facecolor='#f0f0f0', edgecolor='k')

x_1 = np.arange(-10, 10, 0.1)
x_2 = [i for i in range(-10, 10)]
x_3 = np.arange(-10, 10, 0.1)

function_1 = lambda x: np.sin(2 * x)
function_2 = func_2
function_3 = lambda x: np.array(x_3) * 2 + np.sin(2 * x)

axes[0].plot(
    x_1, function_1(x_1),
    label='f(x) = sin(2x)',
    color='#fcba03',
    linewidth=2,
)
axes[0].plot(
    x_2, function_2(x_2),
    label='f(x) = 2х',
    color='#eb363f',
    linewidth=1,
    linestyle='--',
    marker='o',
    markerfacecolor='#9c171e',
    markersize=5,
)
axes[1].plot(
    x_3, function_3(x_3),
    label='f(x) = sin(2x) + 2x',
    linestyle='-.'
)
customize_first_figure(axes[0])
customize_second_figure(axes[1])

plt.ion()
for delay in np.arange(0, np.pi, 0.1):
    plt.clf()

    function_1 = lambda x: np.sin(2 * (x + delay))
    axes[0].plot(
        x_1, function_1(x_1),
        label='f(x) = sin(2x)',
        color='#fcba03',
        linewidth=2,
    )
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.02)

plt.ioff()
plt.show()
