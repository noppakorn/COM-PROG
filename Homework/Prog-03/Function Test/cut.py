def cut(deck, m):
    new_deck = '|'.join(deck.split('|')[2*m:]) + '|'.join(deck.split('|')[:2*m+1])

    return new_deck

assert cut("|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|",4) == "|3H||4H||5H||6H||7H||8H||2H||4S||TD||AC|"
assert cut("|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|",0) == "|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|"
assert cut("|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|",10) == "|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|"