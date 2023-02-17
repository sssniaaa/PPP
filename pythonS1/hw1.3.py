# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input('enter the number of the coordniate plane: '))

if a == 1:
    print('x-coordinated can be 1, 2, 3, 4, 5 and y-coordinates can be 1, 2, 3, 4, 5')
elif a == 2:
    print('x-coordinated can be -1, -2, -3, -4, -5 and y-coordinates can be 1, 2, 3, 4, 5')
elif a == 3:
    print('x-coordinated can be -1, -2, -3, -4, -5 and y-coordinates can be -1, -2, -3, -4, -5')    
elif a == 4:
    print('x-coordinated can be 1, 2, 3, 4, 5 and y-coordinates can be -1, -2, -3, -4, -5')
else:
    print('this plane does not exist')