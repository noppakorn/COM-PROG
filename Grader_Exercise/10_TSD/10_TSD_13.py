win = set()
lose = set()
for i in range(int(input())):
    x = input().split()
    win.add(x[0])
    lose.add(x[1])
print(sorted([i for i in win if i not in lose]))