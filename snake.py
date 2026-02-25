from random import randint
X_SIZE = 10
Y_SIZE = 10

def move():
    key = input()
    result = (0, 0)
    if key == 'w':
        result = (-1, 0)
    elif key == "s":
        result = (1, 0)
    elif key == "a":
        result = (0, -1)
    elif key == "d":
        result = (0, 1)
    return result

def draw_game_field():
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if (x, y) == apple_pos:
                print("🍎", end="")
            elif (x, y) in snake:
                print("🟩", end="")
            elif y in (0, Y_SIZE-1) or x in (0, X_SIZE-1):
                print("⬜", end="")
            else:
                print(" ", end= " ")
        print()

def spawn_apple():
    x = randint(1, X_SIZE - 2)
    y = randint(1, Y_SIZE - 2)
    while (x, y) in snake:
        x = randint(1, X_SIZE-2)
        y = randint(1, Y_SIZE-2)
    return (x, y)

snake = [(X_SIZE//2, Y_SIZE//2)]

apple_pos = spawn_apple()
while True:
    print("\033[2J\033[H", end="")
    draw_game_field()
    direction = move()
    new_pos = (snake[-1][0] + direction[0], snake[-1][1] + direction[1])
    if new_pos[0] in (0, X_SIZE-1) or new_pos[1] in (0, Y_SIZE-1) or new_pos in snake:
        print("YOU LOSE!")
        break
    snake.append((snake[-1][0] + direction[0], snake[-1][1] + direction[1]))
    if new_pos != apple_pos:
        snake.pop(0)
    else:
        apple_pos = spawn_apple()
