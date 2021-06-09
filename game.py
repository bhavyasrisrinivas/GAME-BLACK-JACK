import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
faces = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
         
started = True

class Card:
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face
        
    def __str__(self):
        return self.face+ '---->' + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for face in faces:
                self.deck.append(Card(face, suit))
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        a_card = self.deck.pop()
        return a_card
        
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add(self,card):
        self.cards.append(card)
        self.value += values[card.face]
        if card.face == 'Ace':
            self.aces += 1
    def acevalue(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Coins:
    def __init__(self):
        self.total = 100
        self.bet = 0
        print('\nYour total coins are {} \n'.format(self.total))
        
    def win(self):
        self.total += self.bet
        
    def lose(self):
        self.total -= self.bet
        
def make_bet(coins):
    while True:
        coins.bet = int(input('WHAT IS YOUR BET?\n'))
        if coins.bet > coins.total:
            print('SORRY, YOUR BET CANNOT EXCEED {} \n'.format(coins.total))
        else:
            break
            
def hit(deck,hand):
    hand.add(deck.deal())
    hand.acevalue()

def hit_or_stand(hand):
    global started
    while True:
        a = input("Would you like to Hit or Stand? Enter 'h' or 's'\n")
        if a[0].lower() == 'h':
            hit(deck,hand)
        elif a[0].lower() == 's':
            print("Player stands. Dealer is playing.....\n")
            started = False
        else:
            print("WRONG OPTION\n")
            continue
        break
    
def display(player,dealer):
    print("\nDealer's Hand")
    print("<card hidden>")
    print('', dealer.cards[1])
    print("Dealer Value= ",dealer.value-values[dealer.cards[0].face])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player Value = ", player.value)
    
def displayALL(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)
    
def player_busts(player,dealer,coins):
    print("Player busts!\n")
    coins.lose()
    
def player_wins(player,dealer,coins):
    print("Player wins!\n")
    coins.win()
    
def dealer_busts(player,dealer,coins):
    print("Dealer busts!\n")
    coins.win()
    
def dealer_wins(player,dealer,coins):
    print("Dealer wins!\n")
    coins.lose()
    
def push(player,dealer):
    print("! It's a push (tie for both).\n")
    
    
while True:
    print("\t\t************                   WELCOME TO BLACKJACK GAME                 ************")
    player_coins = Coins()
    make_bet(player_coins)
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    player_hand.add(deck.deal())
    player_hand.add(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add(deck.deal())
    dealer_hand.add(deck.deal())
    display(player_hand, dealer_hand)
    
    while started:
        hit_or_stand(player_hand)
        display(player_hand,dealer_hand) 
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_coins)
            print("\nPlayer busts so remaining coins are ", player_coins.total)
            print("\nDealer Wins\n")
            break
    if player_hand.value <= 21:
        while dealer_hand.value <17:
            hit(deck, dealer_hand)
        displayALL(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_coins)
            print("\nDealer busts\n\nPlayer wins\n So remaining coins are ", player_coins.total)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_coins)
            print("\nDealer Wins\n\nPlayer loses\n so remaining coins are ", player_coins.total)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_coins)
            print("\nPlayer wins\n so remaining coins are ", player_coins.total)
        else:
            push(player_hand,dealer_hand)
            print("\nYou are at push, and the remaining coins are ", player_coins.total)
    new_game = input("would you like to play again? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('THANKYOU!')
        break
