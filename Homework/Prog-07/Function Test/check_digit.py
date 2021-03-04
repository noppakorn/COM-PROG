def check_digit(digits):
    su,m,v = 0,10,[1,3]*6
    for i in range(len(digits)) : su += int(digits[i])*v[i]
    while m < su : m += 10
    return str(m - su)

print(check_digit('321029204519'))
print(check_digit('123456789018'))
