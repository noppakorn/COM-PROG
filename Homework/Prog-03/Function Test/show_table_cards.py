cards = '|2H||3H||4H||5H|'

def show_table_cards(cards, m):
    table = 'Table: ' + '....'*min(max(0,len(cards.split('|')[1::2])-m),1) + '|'.join(cards.split('|')[-2*m-1:])
    print('-'*len(table))
    print(table)
    print('-'*len(table))

# Test Cases from PDF
show_table_cards(cards,5)
show_table_cards(cards,4)
show_table_cards(cards,3)
show_table_cards(cards,2)

# Special Test Case for very high index
show_table_cards(cards,1000)