from random import randint

number = randint(1,100)
print('Угайдайте число от 1 до 100')

while True:

    guess = int(input('введите число: '))

    if guess < number:
        print('Ваше число меньше того что загадано.')
    

    if guess > number:
        print('ваше число больше того что загадано.')
    
    if guess == number:

        break

print('Отличная интуиция! Вы угадали число. :)')
