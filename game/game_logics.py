import os, random
from ascii_graphics import card
from art import *
from colorama import Fore, Back, Style

cards_nominal = ('2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K", "A")
cards_dict = {'2': 2, 
              '3': 3, 
              '4': 4, 
              '5': 5, 
              '6': 6, 
              '7': 7, 
              '8': 8, 
              '9': 9, 
              '10': 10, 
              "J": 11, 
              "Q": 12, 
              "K": 13, 
              "A": 1  }


def clear():
    os.system(['clear','cls'][os.name == 'nt'])


def lines():
    print('  ', '-' * 48)


def start():
    clear()
    print()
    print(Fore.WHITE)
    print(text2art("blackjack"))
    lines()
    print(Fore.RED + '    We remind you that gambling is very, very bad!')
    print(Fore.WHITE)


def card_generate():
    return random.choice(cards_nominal)


def generate_card_stack():
    card_stack = []
    for _ in range(4):
        card_stack.extend(list(cards_nominal))
    random.shuffle(card_stack)
    return card_stack


def player_turn(player_cards, game_status):
    print('[d] - draw another card')
    print('[s] - stop, keep the cards')
    
    turn = input('> ')
    match turn:
        case 'd':
            new_card = card_generate()
            player_cards.append(new_card)
        case 's':
            game_status = False
        case '_':
            pass
    
    return player_cards, game_status


def dealer_bet(bank, player_bet):
    while True:
        dealer_bet = random.randint(player_bet//2, player_bet*2)
        if dealer_bet <= bank:
            break

    bank = bank - dealer_bet
    return dealer_bet, bank


def player_bet(player_money):
    while True:
        clear()
        print(f"Make your's bet! Total: {player_money}")
        bet = input("> ")
        if bet.isdigit() == True:
            bet = int(bet)
            if bet <= player_money and bet != 0:
                player_money -= bet
                break
    return bet, player_money


def cards_deal(start=False, list_cards=[]):
    '''Generating cards and summing score. If start=True generates two cards.'''
    score = 0
    if start == True:
        list_cards = []
        list_cards.append(card_generate())
        list_cards.append(card_generate())

    for i in range(len(list_cards)):
        score += cards_dict[list_cards[i]]

    return list_cards, score


def end_game():
    clear()
    print('You bankrupted the Dealer!')
    print('Are you happy now?')
    print('')
    input('> Start New Game')
