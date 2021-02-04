def cut(deck, m):
    new_deck = '|'.join(deck.split('|')[2*m:]) + '|'.join(deck.split('|')[:2*m+1])

    return new_deck