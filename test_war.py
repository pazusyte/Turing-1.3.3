import pytest

ranks_order = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']

def test_total_cards():
    from war import Deck 

    deck = Deck()
    assert len(deck.cards) == 52, "Total number of cards is not 52"

if __name__ == "__main__":
    pytest.main()
