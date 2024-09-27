# BlackJack console card game in Python
![изображение](https://github.com/user-attachments/assets/8acf3a9a-9d3d-444c-961a-00c3f0fa036e)

This is the simplest interpretation of the Blackjack game in the Python programming language. 

The game has a player and a dealer. Before the game starts, they both make bets. The dealer makes a bet randomly in the range from half the player's bet to two bets of the player. 
Afterwards, both have two cards. One of the dealer's cards is hidden. The player's victory consists in the player collecting more points than the dealer or collecting 21 points.
If the player scores less than the dealer or more than 21 points, the player loses.

![изображение](https://github.com/user-attachments/assets/0f87818d-04e2-4a26-a128-6f75567c5f7f)

Each "card" has its own numerical value:
[2] : 2 
[3] : 3 
[4] : 4 
[5] : 5 
[6] : 6 
[7] : 7 
[8] : 8
[9] : 9
[10] : 10 
[J] : 11 
[Q] : 12 
[K] : 13 
[A] : 1  

The only ending to the game is the dealer going *bankrupt*.

**Notes:**
> In the future, I might finish the ASCII graphics for this console game. For now, ascii_graphics.py is pretty much useless.

> There is also a deck generator in the game code, but it is not implemented ```generate_card_stack()```.  The player and the dealer are currently given random cards, which means that the game (purely theoretically) can get 10 "A" cards.

> If you lose all your money and your money balance = 0, you will be stuck in the bet menu forever. That's the **punishment** for gambling lol. (Fine, I'll fix that one day.) 
