# Prog-04: Mastermind Game 
# 6330258021 Noppakorn Jiravaranun

import random
import math

WINNING_MSG = "Congratulations! You won the game."
LOSING_MSG = "Sorry! You just lost it."

code = ''.join(random.sample('ABCDEF', 4))

print('Please guess the puzzle code using')
print('the four distinct code characters from [A to F]:')

#---------------------------------------------------
codel = list(code)
w = False

g = list(input('Turn #1 : '))
if g == codel : 
    print(WINNING_MSG)
    w = True
else :
    P,V = 0,0
    if g[0] == codel[0] : P += 1
    if g[1] == codel[1] : P += 1
    if g[2] == codel[2] : P += 1
    if g[3] == codel[3] : P += 1
    if g[0] in codel : V += 1
    if g[1] in codel : V += 1
    if g[2] in codel : V += 1
    if g[3] in codel : V += 1
    V -= P
    X = 4-P-V
    print(' '*10+'P='+str(P)+',V='+str(V)+',X='+str(X))

if not w :
    g = list(input('Turn #2 : '))
    if g == codel : 
        print(WINNING_MSG)
        w = True
    else :
        P,V = 0,0
        if g[0] == codel[0] : P += 1
        if g[1] == codel[1] : P += 1
        if g[2] == codel[2] : P += 1
        if g[3] == codel[3] : P += 1
        if g[0] in codel : V += 1
        if g[1] in codel : V += 1
        if g[2] in codel : V += 1
        if g[3] in codel : V += 1
        V -= P
        X = 4-P-V
        print(' '*10+'P='+str(P)+',V='+str(V)+',X='+str(X))

if not w :
    g = list(input('Turn #3 : '))
    if g == codel : 
        print(WINNING_MSG)
        w = True
    else :
        P,V = 0,0
        if g[0] == codel[0] : P += 1
        if g[1] == codel[1] : P += 1
        if g[2] == codel[2] : P += 1
        if g[3] == codel[3] : P += 1
        if g[0] in codel : V += 1
        if g[1] in codel : V += 1
        if g[2] in codel : V += 1
        if g[3] in codel : V += 1
        V -= P
        X = 4-P-V
        print(' '*10+'P='+str(P)+',V='+str(V)+',X='+str(X))

if not w :
    g = list(input('Turn #4 : '))
    if g == codel : 
        print(WINNING_MSG)
        w = True
    else :
        P,V = 0,0
        if g[0] == codel[0] : P += 1
        if g[1] == codel[1] : P += 1
        if g[2] == codel[2] : P += 1
        if g[3] == codel[3] : P += 1
        if g[0] in codel : V += 1
        if g[1] in codel : V += 1
        if g[2] in codel : V += 1
        if g[3] in codel : V += 1
        V -= P
        X = 4-P-V
        print(' '*10+'P='+str(P)+',V='+str(V)+',X='+str(X))
        print(LOSING_MSG)
        print('The answer is ',code)
        print('Please try again...')