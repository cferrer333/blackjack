import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
    def deal_one(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1
    def ace_adjuster(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Player(Hand):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Dealer(Hand):
    def __init__(self, name):
        self.name = name
        super().__init__()

# Driver code to define methods of the game
def show_some():
        print("\nDealer's Hand:")
        print(dealer.cards[1])
        print("Your Hand:")
        for card in player.cards:
            print(card)
        print(f"Value: {player.value}")
def show_all():
    print("\nDealer's Hand:")
    for card in dealer.cards:
        print(card)
    print(f"Value: {dealer.value}")
    print("Your Hand:")
    for card in player.cards:
        print(card)
    print(f"Value: {player.value}")
def hit_or_stand():
    global playing
    while True:
        response = input("\nWould you like to hit or stand? Enter 'h' or 's' ")
            
        if response[0].lower() == 'h':
            hit()
            show_some()
            if player.value > 21:
                player_busts()
                break
            elif player.value == 21:
                player_wins()
                playing = False
                break
        elif response[0].lower() == 's':
            print("Player stands. Dealer is playing..." + "\n")
            show_all()
            if dealer.value > 21:
                dealer_busts()
                playing = False
                break
            elif dealer.value > player.value:
                dealer_wins()
                playing = False
                break
            elif dealer.value < player.value:
                player_wins()
                playing = False
                break
            else:
                push()
                playing = False
                break
        else:
            print("Sorry, invalid entry.")
            hit_or_stand()
def hit():
    player.add_cards(deck.deal_one())
    player.ace_adjuster()
def player_wins():
    if player.value > dealer.value and player.value <= 21:
        show_all()
        print("Player wins!")
def dealer_wins():
    if dealer.value >= player.value and dealer.value <= 21:
        show_all()
        print("Dealer wins!")
def player_busts():
    if player.value > 21:
        show_all()
        print("Player busts!")
        print("Dealer wins!")
def dealer_busts():
    if dealer.value > 21:
        show_all()
        print("Dealer busts!")
        print("Player wins!")
def push():
    if player.value == dealer.value:
        print("Dealer and player tie! It's a push.")
while True:
    print('\nWelcome to Blackjack!')
    response = input("Would you like to play? Enter 'y' or 'n' ")
    if response[0].lower() == 'n':
        break
    elif response[0].lower() == 'y':
        playing = True
    else:
        print("Sorry, please try again.")

    deck = Deck()
    hand = Hand()
    player = Player('player1')
    dealer = Dealer('the_dealer')
    deck.shuffle()
    player.add_cards(deck.deal_one())
    player.add_cards(deck.deal_one())
    dealer.add_cards(deck.deal_one())
    dealer.add_cards(deck.deal_one())

    show_some()
    while playing:
        if player.value < 21:
            hit_or_stand()
        if player.value <= 21:
            while dealer.value < 17:
                dealer.add_cards(deck.deal_one())
        playing = False
print("Thanks for playing!")