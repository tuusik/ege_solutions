import os
import time
import random

width = 10
height = 20

shapes = [
    [['0', '0', '0', '0']],
    [['0', '0'], ['0', '0']],
    [['0', '0', '0'], ['.', '.', '0']],
    [['0', '0', '0'], ['0', '.', '.']],
    [['0', '0', '.'], ['.', '0', '0']],
    [['.', '0', '0'], ['0', '0', '.']],
    [['0', '.', '.'], ['0', '0', '0']]
]

def create_field():
    return [['.' for _ in range(width)] for _ in range(height)]

field = create_field()

def print_field():
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in field:
        print('|' + ''.join(row) + '|')
    print('-' * (width + 2))
    print("Введите команду: a (влево), d (вправо), w (повернуть), s (ускорить падение), q (выход)")

def print_field_with_temp(temp_field):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in temp_field:
        print('|' + ''.join(row) + '|')
    print('-' * (width + 2))
    print("Введите команду: a (влево), d (вправо), w (повернуть), s (ускорить падение), q (выход)")

def check_collision(shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell == '0':
                xi = x + j
                yi = y + i
                if xi < 0 or xi >= width or yi >= height:
                    return True
                if yi >= 0 and field[yi][xi] == '0':
                    return True
    return False

def merge_shape(shape, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell == '0':
                if 0 <= y + i < height and 0 <= x + j < width:
                    field[y + i][x + j] = '0'

def clear_lines():
    global score
    new_field = [row for row in field if '.' in row]
    cleared = height - len(new_field)
    for _ in range(cleared):
        new_field.insert(0, ['.' for _ in range(width)])
    field[:] = new_field
    score += cleared * 100

def rotate(shape):
    return [list(row) for row in zip(*shape[::-1])]

def spawn_new_shape():
    shape = random.choice(shapes)
    x = width // 2 - len(shape[0]) // 2
    y = 0
    return shape, x, y

score = 0
current_shape, current_x, current_y = spawn_new_shape()

while True:
    # Создаем временное поле с текущей фигурой для отображения
    temp_field = [row[:] for row in field]
    for i, row in enumerate(current_shape):
        for j, cell in enumerate(row):
            if cell == '0':
                yi = current_y + i
                xi = current_x + j
                if 0 <= yi < height and 0 <= xi < width:
                    temp_field[yi][xi] = '0'
    print_field_with_temp(temp_field)
    cmd = input("Команда: ").lower()
    if cmd == 'a':
        if not check_collision(current_shape, current_x - 1, current_y):
            current_x -= 1
    elif cmd == 'd':
        if not check_collision(current_shape, current_x + 1, current_y):
            current_x += 1
    elif cmd == 'w':
        rotated = rotate(current_shape)
        if not check_collision(rotated, current_x, current_y):
            current_shape = rotated
    elif cmd == 's':
        if not check_collision(current_shape, current_x, current_y + 1):
            current_y += 1
    elif cmd == 'q':
        print("Вы вышли из игры.")
        break
    # Автоматическое падение
    if not check_collision(current_shape, current_x, current_y + 1):
        current_y += 1
    else:
        merge_shape(current_shape, current_x, current_y)
        clear_lines()
        current_shape, current_x, current_y = spawn_new_shape()
        if check_collision(current_shape, current_x, current_y):
            print("Игра окончена!")
            break