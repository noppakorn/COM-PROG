x = [int(e) for e in input().split()]
y = int(input())
print(x[-y:] + x[:-y])
print(x[y:] + x[:y])