import math
# Ввод координат и радиуса круга
x = float(input("Введите x: "))
y = float(input("Введите y: "))
radius = float(input("Введите радиус : "))
# Вычисление расстояния от точки до начала координат
distance = math.sqrt(x*2 + y*2)
# Проверка на попадание точки в круг
if distance <= radius:
    print("Точка находится в круге") #Вывод результата на экран
else:
    print("Точка находится за кругом") #Вывод результата на экран