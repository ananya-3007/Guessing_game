# Guessing_game

secret_number=50
count_number=1
while count_number<=3:
    guess=int(input('Guess:'))
    count_number=count_number+1
    if guess==secret_number:
        print('You Won')
        break
else:
    print('You have Lost')