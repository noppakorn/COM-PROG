# Prog-06: Jaccard Similarity
# 6330258021 Noppakorn Jiravaranun

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

STOP_WORDS = stopwords.words('english')
STEMMER = PorterStemmer()

def read_tweets():
    f = open('biden.txt', encoding='utf-8')
    tweets = [line.strip() for line in f.readlines()]
    f.close()
    return tweets

def normalize_text( text ):
    words = []
    for w in word_tokenize(text.lower()):
        if w.isalnum() and w not in STOP_WORDS:
            words.append(STEMMER.stem(w))
    return get_unique( words )

def main():
    tweets = read_tweets()
    norm_tweets = []
    for t in tweets:
        norm_tweets.append( normalize_text(t) )

    print_width = 48
    while True:
        query = input('Query words   : ')
        if query == '': break
        n = int(input('No. of results: '))
        norm_query = normalize_text(query)
        top_n = top_n_similarity(norm_tweets, norm_query, n)
        if len(top_n) == 0:
            print('No matches found.')
        else:
            for tid, jc_coef in top_n:
                show_tweet(tid, tweets[tid], jc_coef, print_width)
        print('-' * print_width)

#--------------------------------------------------------
def get_unique( words ):
    unique_words = []
    for i in words :
        if i not in unique_words : unique_words.append(i)
    return unique_words

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
    top_n = top_n[:-n-1:-1]
    return top_n

def show_tweet(tweet_id, tweet_content, jc_coef, print_width):
    print('\n#'+str(tweet_id),'('+str(round(jc_coef,2))+')')
    s = [' ']
    for i in tweet_content.split(' ') :
        n = len(' '.join(s))
        if n+len(i)+1 <= print_width : s.append(i)
        if n+len(i)+1 > print_width : 
            print(' '.join(s))
            s = [' ',i]
    print(' '.join(s))
#--------------------------------------------
main()
