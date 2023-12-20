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


class CardGame:
    def __init__(self):
        self.deck = Deck() 
        self.player = Player("Player")
        self.program = Player("Program")

    def display_winner(self, winner):
        print(
            f"{winner} wins!\nPlayer cards: {len(self.player.hand)}, Program cards: {len(self.program.hand)}\n"
        )

    @staticmethod
    def compare_cards(player_card, program_card):
        ranks_order = ranks[::-1]

        if ranks_order.index(player_card.rank) > ranks_order.index(program_card.rank):
            return "Player"
        elif ranks_order.index(player_card.rank) < ranks_order.index(program_card.rank):
            return "Program"
        else:
            return "War"

    @staticmethod
    def check_cards_for_war(player_card_hand, program_card_hand):
        if len(player_card_hand) < 2:
            return "Program"
        elif len(program_card_hand) < 2:
            return "Player"
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
            # to check if player and program have enough cards to play for the war.
        else:
            self.card_game.display_winner(winner)

    def resolve_war(self, player_card_hand, program_card_hand):
        print("War!\n")

        if CardGame.check_cards_for_war() == "war":
            face_down_player_card = self.card_game.player.place_card()
            face_down_program_card = self.card_game.program.place_card()
            face_up_player_card = self.card_game.player.place_card()
            face_up_program_card = self.card_game.program.place_card()

            
        else:
            pass


if __name__ == "__main__":
    main()
