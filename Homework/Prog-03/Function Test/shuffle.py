def shuffle(deck) :
    ds = deck.split('|')[1::2]
    n = len(ds)
    ldeck = ['']*n
    ldeck[::2],ldeck[1::2] = ds[:(n//2)+(n%2)],ds[(n//2)+(n%2):]
    new_deck = '|' + '||'.join(ldeck) + '|'
    return new_deck

# main test
odeck = "|2H||3H||4H||5H||6H||7H||8H||9H||TH||JH||QH||KH||AH|"
edeck = "|2H||3H||4H||5H||6H||7H||8H||9H||TH||JH||QH||KH|"
print(shuffle(odeck))
print(shuffle(edeck))
assert shuffle(odeck) == "|2H||9H||3H||TH||4H||JH||5H||QH||6H||KH||7H||AH||8H|"
assert shuffle(edeck) == "|2H||8H||3H||9H||4H||TH||5H||JH||6H||QH||7H||KH|"

#special test
odeck3 = "|2H||3H||4H|"
odeck5 = "|2H||3H||4H||5H||6H|"
print('-------------')
print(shuffle(odeck3))
print(shuffle(odeck5))