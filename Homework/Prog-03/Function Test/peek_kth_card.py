def peek_kth_card(cards, k):
    the_kth_card = '|'.join(cards.split('|')[2*k-2:2*k+1])

    return the_kth_card