import random

ranks = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
symbols = ["hearts", "spades", "diamonds", "clubs"]

class Card:
    def __init__(self, rank, symbol):
        self.rank = rank
        self.symbol = symbol

    def __str__(self):
        return f"{self.rank} of {self.symbol}"

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

    def add_cards(self, cards):
        self.hand.extend(cards)

def compare_cards(player_card, program_card, ranks_order):
    if ranks_order.index(player_card.rank) > ranks_order.index(program_card.rank):
        return "Player"
    elif ranks_order.index(player_card.rank) < ranks_order.index(program_card.rank):
        return "Program"
    else:
        return "War"

def display_winner(winner, player, program):
    print(f"{winner} wins!\nPlayer cards: {len(player.hand)}, Program cards: {len(program.hand)}\n")

def resolve_war(player, program, ranks_order, player_card, program_card):
    print("War!\n")

    cards_to_add_to_hand = [player_card, program_card]

    while True:
        if len(player.hand) < 2 or len(program.hand) < 2:
            break

        face_down_player_card = player.place_card()
        face_down_program_card = program.place_card()

        print(f"Player places card facing down, Program places card facing down")

        face_up_player_card = player.place_card()
        face_up_program_card = program.place_card()

        print(f"Player places {face_up_player_card}, Program places {face_up_program_card}")

        cards_to_add_to_hand.extend([face_down_player_card, face_down_program_card, face_up_player_card, face_up_program_card])

        war_winner = compare_cards(face_up_player_card, face_up_program_card, ranks_order)

        if war_winner is not None:
            player.add_cards(cards_to_add_to_hand)
            display_winner(war_winner, player, program)

        if war_winner != "War":
            break

def main():
    deck = Deck()
    player = Player("Player")
    program = Player("Program")
    ranks_order = ranks[::-1]

    player.hand = deck.deal(26)
    program.hand = deck.deal(26)

    while player.hand and program.hand:
        try:
            input("Press Enter to place a card\n")
        except EOFError:
            break
        
        player_placed_card = player.place_card()
        program_placed_card = program.place_card()

        print(f"Player places {player_placed_card}, Program places {program_placed_card}")

        winner = compare_cards(player_placed_card, program_placed_card, ranks_order)
        if winner == "War":
            resolve_war(player, program, ranks_order, player_placed_card, program_placed_card)
        else:
            cards = [player_placed_card, program_placed_card]
            winner_obj = player if winner == "Player" else program
            winner_obj.add_cards(cards)
            display_winner(winner, player, program)

if __name__ == "__main__":
    main()
