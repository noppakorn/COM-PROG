def f3(x) : return x+10
def f1(x) :
    def f2(x) : return x+2
    print(x,f3(x),f2(f3(x)))
f1(5)