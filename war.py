import random

ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
symbols = ["hearts", "spades", "diamonds", "clubs"]

def main():
    game = CardGame()
    play = Play(game)

    player_hand = game.player.hand = game.deck.deal(26)
    program_hand = game.program.hand = game.deck.deal(26)

    while player_hand and program_hand:
        play.play_round()

    if not player_hand:
        print("Player ran out of cards. Program wins!")
    else:
        print("Program ran out of cards. Player wins!")

class Card:
    def __init__(self, rank, symbol):
        self.rank = rank
        self.symbol = symbol

    def __str__(self):
        return f'{self.rank} of {self.symbol}'

class Deck:
    def __init__(self):  
        self.cards = [Card(rank, symbol) for rank in ranks for symbol in symbols]
        random.shuffle(self.cards)

    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def place_card(self):
        return self.hand.pop(0)

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.program = Player("Program")

    def display_winner(self, winner):
        print(f'{winner} wins!\nPlayer cards: {len(self.player.hand)}, Program cards: {len(self.program.hand)}\n')
    
    @staticmethod
    def compare_cards(player_card, program_card):
        ranks_order = ranks[::-1]

        if ranks_order.index(player_card.rank) > ranks_order.index(program_card.rank):
            return "Player"
        elif ranks_order.index(player_card.rank) < ranks_order.index(program_card.rank):
            return "Program"
        else:
            return "War"

class Play:
    def __init__(self, card_game):
        self.card_game = card_game

    def play_round(self):
        input("Press Enter to place a card\n")

        player_card = self.card_game.player.place_card()
        program_card = self.card_game.program.place_card()

        print(f"Player places {player_card}, Program places {program_card}")

        winner = CardGame.compare_cards(player_card, program_card)

        if winner == "War":
            resolve_war()
        else:
            self.card_game.display_winner(winner)

def resolve_war():
    print("War!\n")

if __name__ == "__main__":
    main()
