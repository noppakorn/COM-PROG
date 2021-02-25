def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    N += 1
    while not is_prime(N) : N+=1
    return N

def next_twin_prime(N):
    N += 1
    while not (is_prime(N) and is_prime(N+2)) : N += 1
    return N,N+2
    
exec(input().strip()) 