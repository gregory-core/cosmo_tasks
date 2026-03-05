import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        W,H,R = input().split()
        W = int(W)
        H = int(H)
        R = int(R)
        if 2*R>W:
            print("NO")
        elif 2*R>H:
            print("NO")
        else:
            print("YES")
    except EOFError:
        break
