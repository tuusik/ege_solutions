X_SIZE = 40
Y_SIZE = 20

ball_xcor = 20
ball_ycor = 10
l_racket_cor = 9
r_racket_cor = 9

def move_racket(l_racket, r_racket):
    move = input()
    rackets = [l_racket, r_racket]
    if move == "a" and l_racket != 1:
        rackets = [l_racket-1, r_racket]
    elif move == "z" and l_racket != 16:
        rackets = [l_racket+1, r_racket]
    elif move == "k" and r_racket != 1:
        rackets = [l_racket, r_racket-1]
    elif move == "m" and r_racket != 16:
        rackets = [l_racket, r_racket+1]
    return rackets

def draw_game_field():
    for i in range(Y_SIZE):
        for j in range(X_SIZE):
            if j == 2 and i in [l_racket_cor, l_racket_cor+1, l_racket_cor+2]:
                print("|", end=" ")
            elif j == 37 and i in [r_racket_cor, r_racket_cor+1, r_racket_cor+2]:
                print("|", end=" ")
            elif i == ball_ycor and j == ball_xcor:
                print("*", end=" ")
            elif i in (0, 19) and j != 39:
                print("#", end="#")
            elif j in (0, 39):
                print("#", end="")
            elif j == 20:
                print("^", end=" ")
            else:
                print(" ", end=" ")
        print()
    print(f"left: {left_p}, right: {right_p}")

left_p = 0
right_p = 0

vector_x = 1
vector_y = 1
while True:
    print("\033[2J\033[H", end="")
    draw_game_field()
    l_racket_cor, r_racket_cor = move_racket(l_racket_cor, r_racket_cor)
    ball_ycor += vector_y
    ball_xcor += vector_x
    if ball_xcor == 2 and ball_ycor in [l_racket_cor, l_racket_cor+1, l_racket_cor+2]:
        vector_x *= -1
    if ball_xcor == 37 and ball_ycor in [r_racket_cor, r_racket_cor+1, r_racket_cor+2]:
        vector_x *= -1
    if ball_ycor == 1 or ball_ycor == 18:
        vector_y *= -1
    if ball_xcor == 0:
        right_p += 1
        ball_xcor = 20
        ball_ycor = 10
        vector_x *= -1
        vector_y *= -1
    if ball_xcor == 39:
        left_p += 1
        ball_xcor = 20
        ball_ycor = 10
        vector_x *= -1
        vector_y *= -1
