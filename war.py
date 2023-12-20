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


class GameProcess:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.program = Player("Program")

    def play_round(self):
        input("Press Enter to place a card\n")

        player_placed_card = self.player.place_card()
        program_placed_card = self.program.place_card()

        print(f"Player places {player_placed_card}, Program places {program_placed_card}")

        self.compare_cards(player_placed_card, program_placed_card)

        return self.player.hand, self.program.hand

    def compare_cards(self, player_card, program_card):
        ranks_order = ranks[::-1]

        if ranks_order.index(player_card.rank) > ranks_order.index(program_card.rank):
            self.add_cards_to_hands("Player", player_card, program_card)
        elif ranks_order.index(player_card.rank) < ranks_order.index(program_card.rank):
            self.add_cards_to_hands("Program", player_card, program_card)
        else:
            self.resolve_war()

    def add_cards_to_hands(self, winner, player_card, program_card):
        if winner == "Player":
            self.player.add_cards([player_card, program_card])
        elif winner == "Program":
            self.program.add_cards([player_card, program_card])

        self.display_winner(winner)
        return winner

    def display_winner(self, winner):
        print(f"{winner} wins!\nPlayer cards: {len(self.player.hand)}, Program cards: {len(self.program.hand)}\n")

    def resolve_war(self):
        print("War!\n")

        while True:
            if self.check_cards_for_war() == "War":
                face_down_player_card = self.player.place_card()
                face_down_program_card = self.program.place_card()

                face_up_player_card = self.player.place_card()
                face_up_program_card = self.program.place_card()

                war_winner = self.compare_war_cards(face_up_player_card, face_up_program_card)

                if war_winner == "Player":
                    self.player.add_cards([face_down_player_card, face_down_program_card])
                elif war_winner == "Program":
                    self.program.add_cards([face_down_player_card, face_down_program_card])
            else:
                break

    def check_cards_for_war(self):
        if len(self.player.hand) < 2:
            return "Program"
        elif len(self.program.hand) < 2:
            return "Player"
        else:
            return "War"

    def compare_war_cards(self, player_card, program_card):
        ranks_order = ranks[::-1]

        if ranks_order.index(player_card.rank) > ranks_order.index(program_card.rank):
            self.player.add_cards([player_card, program_card])
            return "Player"
        elif ranks_order.index(player_card.rank) < ranks_order.index(program_card.rank):
            self.program.add_cards([player_card, program_card])
            return "Program"
        else:
            return None

def main():
    game = GameProcess()

    player_hand = game.player.hand = game.deck.deal(26)
    program_hand = game.program.hand = game.deck.deal(26)

    while player_hand and program_hand:
        player_hand, program_hand = game.play_round()

    if not player_hand:
        print("Player ran out of cards. Program wins!")
    else:
        print("Program ran out of cards. Player wins!")

if __name__ == "__main__":
    main()

