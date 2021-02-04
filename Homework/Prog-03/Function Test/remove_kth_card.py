def remove_kth_card(cards, k):
    new_cards = '|'.join(cards.split('|')[:2*k-1]+cards.split('|')[2*k+1:])

    return new_cards

print(remove_kth_card("|2H||4S||TD||AC|",2))
assert remove_kth_card("|2H||4S||TD||AC|",2) == "|2H||TD||AC|"

assert remove_kth_card("|2H|",1) == ""