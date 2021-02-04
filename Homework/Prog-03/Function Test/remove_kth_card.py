def remove_kth_card(cards, k):
    new_cards = '|'.join(cards.split('|')[:2*k-1]+cards.split('|')[2*k+1:])

    return new_cards
