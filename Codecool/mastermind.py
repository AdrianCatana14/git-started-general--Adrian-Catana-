import random
colors = 'YORPGB'
secret = ''

# Select the code
n = random.randint(0, 5)
random_letter = colors[n]
secret = ""
for i in range(4):
    n = random.randrange(6)
    secret += colors[n]

# Ask for a guess

guess = input('Make your guess: ')
guess = guess.upper()

guess_is_invalid = True
while guess_is_invalid:
    guess = input('Make your guess: ').upper()
    if len(guess) == 4:
        guess_is_invalid = False
    elif guess == 'BOARD':
        guess_is_invalid = False
        for letter in guess:
            if letter not in colors:
                guess_is_invalid = True
    if guess_is_invalid:
        print('Please write 4-letter words using the characters Y, O, R, P, G, B!')

# Answer the guess 

hits = 0 
for i in range(4):
    if guess[i] == secret[i]:
        hits += 1
close = 0
for color in colors:
    close += min(secret.count(color), guess.count(color))
close = close - hits

# Win or lose
history = []
round = 1
while round <= 12:
    print(f'Round {round}')
    if guess == 'BOARD':
        print()
    else:
        print(f'Hits: {hits} Close: {close}')
    history.append((guess, hits, close))
    print()
    for row in history:
        for color in row[0]:
            print(f" {color}", end="")
        print(f" | {row[1]} {row[2]}")
    print()
    round += 1
if hits == 4:
    print(f'Congratulations, your broke the code! The secret was {secret}. ')
else:
    print(f'You have run out of attempts, you lost the game. The secret was {secret}. ')