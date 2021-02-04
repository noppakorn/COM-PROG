def peek_kth_card(cards, k):
    the_kth_card = '|'.join(cards.split('|')[2*k-2:2*k+1])

    return the_kth_card

print(peek_kth_card("|2H||4S||TD||AC|",2)) 
assert peek_kth_card("|2H||4S||TD||AC|",2) == "|4S|"
assert peek_kth_card("|2H|",1) == "|2H|"