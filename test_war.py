import pytest

from war import Deck, Player, compare_cards, resolve_war, display_winner

ranks_order = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']


def test_total_cards_after_each_round():
    deck = Deck()
    player = Player("Player")
    program = Player("Program")

    player.hand = deck.deal(26)
    program.hand = deck.deal(26)

    while player.hand and program.hand:
        player_placed_card = player.place_card()
        program_placed_card = program.place_card()

        winner = compare_cards(player_placed_card, program_placed_card, ranks_order)
        if winner == "War":
            resolve_war(player, program, ranks_order, player_placed_card, program_placed_card)
        else:
            cards = [player_placed_card, program_placed_card]
            winner_obj = player if winner == "Player" else program
            winner_obj.add_cards(cards)
            display_winner(winner, player, program)

        total_cards_after_round = len(player.hand) + len(program.hand)
        if winner == "War":
            total_cards_after_round += 2
            total_cards_after_round -= 2
        assert total_cards_after_round == 52, f"Total cards after round: {total_cards_after_round}. Expected: 52"

def test_total_cards():
    deck = Deck()
    assert len(deck.cards) == 52, "Total number of cards is not 52"
