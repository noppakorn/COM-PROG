def deal_n_cards(deck, n):
    cards = '|'.join(deck.split('|')[:2*n-1])
    new_deck = '|'.join(deck.split('|')[2*n:])

    return cards, new_deck