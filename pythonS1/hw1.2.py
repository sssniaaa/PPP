# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter x-coordinate on the graph: '))
y = int(input('Enter coordinates of point y on a graph: '))

if x > 0 and y > 0:
    print('plane 1')
elif x < 0 and y > 0:
    print('plane 2')
elif x < 0 and y < 0:
    print('plane 3')
else:
    print('plane 4')