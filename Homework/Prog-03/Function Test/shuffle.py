deck = "|2H||3H||4H||5H||6H||7H||8H||9H||TH||JH||QH||KH||AH|"
def shuffle(deck) :
    print(deck.split('|')[1::2])
    n = len(deck.split('|')[1::2])
    new_deck = 0
    return new_deck

print(shuffle(deck))