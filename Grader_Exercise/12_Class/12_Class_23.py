class Card:
    def __init__(self, value, suit):
        self.value = str(value)
        self.suit = str(suit)
    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'
    def next1(self):
        l = []
        for i in range(3,16):
            s = ('club','diamond','heart','spade')
            for j in range(1,len(s)+1):
                l.append((i,s[j-1]))
        d = {'J':11,'Q':12,'K':13,'A':14,'2':15}
        if self.value in d : v = d[self.value]
        else : v = int(self.value)
        rev = {j:i for i,j in d.items()}
        ind = (l.index((v,self.suit))+1) % 52
        out = l[ind]
        if out[0] in rev : out = rev[out[0]],out[1]
        return Card(*out)
    def next2(self):
        l = []
        for i in range(3,16):
            s = ('club','diamond','heart','spade')
            for j in range(1,len(s)+1):
                l.append((i,s[j-1]))
        d = {'J':11,'Q':12,'K':13,'A':14,'2':15}
        if self.value in d : v = d[self.value]
        else : v = int(self.value)
        rev = {j:i for i,j in d.items()}
        ind = (l.index((v,self.suit))+1) % 52
        out = l[ind]
        if out[0] in rev : out = rev[out[0]],out[1]
        self.value,self.suit = (str(out[0]),str(out[1]))

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])