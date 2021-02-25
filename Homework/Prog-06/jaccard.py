def jaccard(words_1, words_2):
    intersect,union = [],[]
    for i in words_1 : 
        if i in words_2 : intersect.append(i)
    for j in words_1 : union.append(j)
    for k in words_2 : 
        if k not in union : union.append(k)
    jaccard_coef = len(intersect)/len(union)
    return jaccard_coef


words_1 = ['x', 'y', 'z', 'xyz'] 
words_2 = ['y', 'x', 'w']
print(jaccard(words_1,words_2))