cards = '|2H||3H||4H||5H|'

def show_table_cards(cards, m):
    n = len(cards.split('|')[1::2])
    table = 'Table:' + '....'*min(max(0,n-m),1) + '|'.join(cards.split('|')[-2*m-1:])
    print('-'*len(table))
    print(table)
    print('-'*len(table))

show_table_cards(cards,5)
show_table_cards(cards,4)
show_table_cards(cards,3)
show_table_cards(cards,2)