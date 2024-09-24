import time
from game_logics import *
from ascii_graphics import *

player_money = 5000
bank = 150000
run = 0
game = 0

def main():
    global player_money, bank, run, game  

    while not run:
        start()
        time.sleep(2)
        print()
        print("Let's start! (n/y)")
        command = input('> ')
        match command:
            case 'y':
                clear()
                run = 1
            case 'n':
                exit()
            case _:
                continue

    while run:
        ## makings bets
        bet, player_money = player_bet(player_money)
        dealer_money, bank = dealer_bet(bank, bet)
        if dealer_money == 3:
            end_game()
            run = 0
            bank = 150000
            player_money = 500
            break
        
        
        ## generate cards for Player and Dealer
        #card_stack = generate_card_stack() ## TODO: Make cards pop() from card stack
        while True:
            dealer_cards, dealer_score = cards_deal(True)
            player_cards, player_score = cards_deal(True)
            if dealer_score < 21 and player_score < 22:
                break
        
        ## start blackjack
        game = True
        turn = 0
        while game:
            ## cheking player's score every turn
            turn += 1
            _, player_score = cards_deal(False, player_cards)
            clear()
            if player_score >= 21:
                 game = False
                 break
            
            ## dealer's desk
            print(f'     [Turn: {turn}]')
            print(f"Dealer's money: {dealer_money}$")
            print(f'[{dealer_cards[0]}] [?]', end=" ")
            print(f'| score: --')

            print('\n\n\n')

            ## player's desk
            print(f"Your's money: {bet}$")
            print_cards(player_cards)
            print(f'| score: {player_score}')
            print('+', '=' * 20, '+')

            player_cards, game = player_turn(player_cards, game)


        ## ending game, results
        if player_score > 21:    ## lose game: player's score higher than 21
            clear()
            print(f'Your score ({player_score}) bigger than 21.', end=' ')
            print(Fore.RED + f'You lost {bet}$!')
            print(Fore.WHITE)
            bank += dealer_money + bet
            input('> ')
            clear()

        elif dealer_score > player_score: ## lose game: dealer's score higher
            clear()
            print(f"Dealer's score ({dealer_score}) bigger than your's ({player_score})!")
            print()
            print_cards(dealer_cards)
            print(f'| score: {dealer_score}', '[Dealer]')
            print('=' * 24)
            print_cards(player_cards)
            print(f'| score: {player_score}', '[You]')
            print()
            print(Fore.RED + f'You lost {bet}$!')
            print(Fore.WHITE)
            bank += dealer_money + bet
            input('> ')
            clear()

        elif player_score == 21 or dealer_score < player_score:    ## win game
            clear()
            if player_score == 21:
                print(f"Blackjack! Your's score is 21. You Win {dealer_money}$.")
            else:
                print(f"Your's score bigger than Dealer! You win {dealer_money}$.")
            player_money += dealer_money + bet
            print_cards(dealer_cards)
            print(f'| score: {dealer_score}', '[Dealer]')
            print('=' * 24)
            print_cards(player_cards)
            print(f'| score: {player_score}', '[You]')
            input('> ')
            clear()
        
            




if __name__ == "__main__":
    main()