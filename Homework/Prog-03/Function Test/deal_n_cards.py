def deal_n_cards(deck, n):
    cards = '|'.join(deck.split('|')[:2*n+1])
    new_deck = '|'.join(deck.split('|')[2*n:])

    return cards, new_deck

print(deal_n_cards("|2H||4S||TD||AC||AD||AS|",4))

a,b = deal_n_cards("|2H||4S||TD||AC||AD||AS|",4) 
print(a)
assert a == "|2H||4S||TD||AC|" 
assert b == "|AD||AS|"