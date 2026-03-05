import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        a,b,c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        C = a//2
        H = b//6
        O = c//1
        print(min(C,H,O))
    except EOFError:
        break