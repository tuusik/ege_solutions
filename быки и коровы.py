import random

def generate_secret():
    digits = list('0123456789')
    random.shuffle(digits)
    return ''.join(digits[:6])

def check_guess(secret, guess):
    bulls = 0
    cows = 0
    for i in range(6):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    secret = generate_secret()
    print("Я загадал шестизначное число, сможещь отгадать)?")
    
    attempts = 0
    while True:
        guess = input("Введи свои циферки :3 ъхъхъхъ")
        if len(guess) != 6 or not guess.isdigit() or len(set(guess)) != 6:
            print("введи только 6 уникальных цифр.")
            continue
        
        attempts += 1
        bulls, cows = check_guess(secret, guess)
        print(f"Быков: {bulls} Коров: {cows}")
        
        if bulls == 6:
            print(f"а ты хорош!  Угадал число {secret} всего то за {attempts} попыток.")
            break

if __name__ == "__main__":
    play_game()


