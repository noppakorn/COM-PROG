def show_tweet(tweet_id, tweet_content, jc_coef, print_width):
    print('\n#'+str(tweet_id),'('+str(round(jc_coef,2))+')')
    s = []
    for i in tweet_content.split(' ') :
        n = len(' '.join(s))
        if n+len(i)+3 <= print_width : s.append(i)
        if n+len(i)+3 > print_width : 
            print(' ',' '.join(s).strip())
            s = [i]
    print(' ',' '.join(s).strip())

t = 'I promise you that as president, I will always appeal to the best  in us.'
print('1234567890123456789012345678901234567890')
show_tweet(1076,t,0.222222222,30)