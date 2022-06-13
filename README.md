# Курсовая работа по языку Python

Для создания виртуального окружения воспользуемся `virtualenv`. Создавать следует в корневой папке проекта:
```
virtualenv -p 3.10.4 venv
```
Активируем его:
```
. venv/bin/activate
```
Установим все необходимые пакеты из файла `requirements.txt`:
```
pip install -r requirements.txt
```

#### №1. Создание рисунка. Использование библиотеки [Turtle](https://docs.python.org/3/library/turtle.html).
---
Выбрать изображение (произвольно). С помощью библиотеки turtle нарисовать похожее на изображении рисунок. В рисунке должны присутствовать разные графические элементы: 
* круг
* прямоугольник
* треугольник
* дуга и т.п. 

Оценивается сложность рисунка и качество исполнения. Максимальное количество баллов – 30. Дополнительные 5 баллов можно получить, добавив любую анимацию.

#### №2. Построение графиков функций. Использование библиотек [matplotlib](https://matplotlib.org/) и [numpy](https://numpy.org/).
---
Построить графики функций для значений аргументов из интервала (-10.0; +10.0) – интервал выбрать произвольно для лучшего отображения графиков.
1. Использовать функцию random для выбора двух целых значений из интервала [1; 8].
2. В соответствии с выбранными значениями построить в одном окне графики Функции\_1 и Функции\_2.

|   | Функция\_1 | Функция\_2 |
| - | ---------- | ---------- |
| 1 | sin(2x) | 0.5x - 1 |
| 2 | cos(3/x) | 2x + 1 |
| 3 | 2sin(x) | 3x - 2 |
| 4 | -2cos(x) | 2.5x |
| 5 | cos(2x) | 2x - 4 |
| 6 | -3sin(x) | 0.4x + 3 |
| 7 | 0.5sin(x) | -2x + 1 |
| 8 | -cos(x/2) | -3x - 2 |

3. Во втором окне построить график функции, являющийся суммой двух выбранных графиков соответственно в таблице выще.
4. для Функции_1 сделать эффект анимации. Можно использовать специальный класс `FuncAnimation`, или с помощью циклического обновление графика.

Использовать и показать в программных кодах:
* несколько способов генерации аргумента
* использование функции пользователя
* использование lambda-функции

Оценивается качество выполнения задания. Максимальное количество баллов за задания №1-3 – 30. Дополнительные 5 баллов – при выполнении задания №4.

#### №3. Построение столбцовых диаграмм. Использование библиотек [pandas](https://pandas.pydata.org/) и [matplotlib](https://matplotlib.org/).
---
1. Создать объект `Series` из 12 случайных чисел от 0 до 1, индекс – номер по порядку. На основе `Series` создать в одном окне две столбцовые диаграммы в двух подграфиках: одну – вертикальную (с индексами по оси Х), вторую – горизонтальную (с индексами по оси У). Выбрать разные цвета для этих диаграмм.
2. Создать объект `DataFrame` (5х3) из случайных чисел от 0 до 1, индекс – номер по порядку. Дать название объекту и столбцам (в порядка: С, В, А) . Построить столбцовую диаграмму (цвета столбцов – по умолчанию).
3. На основе объекта `DataFrame` из пункта №2 построить сложенную столбиковую диаграмму.
4. Построить диаграмму столбцов в алфавитном порядке и с наклоненными метками на осях. Добавить название графика.

Оценивается качество выполнения задания. Максимальное количество баллов за задания №1-3 – 25. Дополнительные 5 баллов – при выполнении задания №4.
