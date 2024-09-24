import time
#from game_logics import cards_nominal

card = """
 _______
|       |
|       |
|   &   |
|       |
|_______|
"""

def print_cards(list_of_cards_nominals):
    list_cards = []
    for n in list_of_cards_nominals:
        list_cards.append(f'[{n}]')
    print(*list_cards, end=" ")

def dot_animation(): ## NOT USED
    print('.', end='')
    time.sleep(2)
    print('.', end='')
    time.sleep(2)
    print('.', )