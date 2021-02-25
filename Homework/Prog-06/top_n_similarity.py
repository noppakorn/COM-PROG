def jaccard(words_1, words_2):
    intersect,union = [],[]
    for i in words_1 : 
        if i in words_2 : intersect.append(i)
    for j in words_1 : union.append(j)
    for k in words_2 : 
        if k not in union : union.append(k)
    jaccard_coef = len(intersect)/len(union)
    return jaccard_coef

def top_n_similarity(norm_tweets, norm_query, n):
    top_n = []
    for i in range(len(norm_tweets)) :
        jac = jaccard(norm_tweets[i],norm_query)
        if jac > 0 : top_n.append([jac,i])
    top_n.sort()
    for i in top_n : i[0],i[1] = i[1],i[0]
    top_n = top_n[::-1]
    c,l,li,jl = 0,[],[],[]
    for i in range(len(top_n)) :
        if top_n[i][1] == c : li.append(top_n[i][0])
        else : 
            if len(li) != 0 : l.append(sorted(li))
            li = []
            c = top_n[i][1]
            jl.append(c)
            li.append(top_n[i][0])
    l.append(sorted(li))
    top_n = []
    for i in range(len(jl)) :
        for j in l[i] : top_n.append([j,jl[i]])
    return top_n


norm_tweets = [['covid','econom','crisi'],['covid','x','z'],['covid','econom','crisi'],['covid','x','z']]

norm_tweets = [['covid','econom','crisi'],['covid','x','z']]
norm_query = ['covid', 'econom', 'crisi']
n = 3
print(top_n_similarity(norm_tweets, norm_query, n))