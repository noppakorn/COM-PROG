def get_unique( words ):
    unique_words = []
    for i in words :
        if i not in unique_words : unique_words.append(i)
    return unique_words

def jaccard(words_1, words_2):
    union,intersect = get_unique(words_1+words_2),[]
    for i in get_unique(words_1) : 
        if i in get_unique(words_2) : intersect.append(i)
    jaccard_coef = len(intersect)/len(union)
    return jaccard_coef


words_2 = ['covid','covid','a'] 
words_1 = ['covid']
print(jaccard(words_1,words_2))