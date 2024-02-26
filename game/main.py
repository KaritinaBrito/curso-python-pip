import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = (input('piedra, papel o tijera => '))
    user_option = user_option.lower()

    if not user_option in options:
        print("esa opcion no es valida")
        return None, None
        # continue

    computer_option = random.choice(options)

    print('user options => ', user_option)
    print('computer options => ', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('ganaste!, piedra gana a tijera')
            user_wins += 1
        else:
            print('perdiste!, papel gana a piedra')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('ganaste!, papel gana a piedra')
            user_wins += 1
        else:
            print('perdiste!, tijera gana a papel')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'piedra':
            print('perdiste!, piedra gana a tijera')
            computer_wins += 1
        else:
            print('ganaste!, tijeras le gana a papel')
            user_wins += 1

    return user_wins, computer_wins

def win_game(user_wins, computer_wins):
    if computer_wins == 2:
        print('el rotundo ganador es la computadora')
        exit()
    if user_wins == 2: 
        print('El ganador es el usuario')
        exit()

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:  
        print('*'*10)
        print('ROUND', rounds)  
        print('*' * 10)

        print('user_wins', user_wins)
        print('computer wins', computer_wins)

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        win_game(user_wins, computer_wins)
        rounds += 1

run_game()