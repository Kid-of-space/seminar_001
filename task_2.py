# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input("Введите проходимое  расстояние за день: "))
m = int(input("Введите расстояние которое необходимо пройти: "))
import math
result  = (m / n)
print(math.ceil(result))