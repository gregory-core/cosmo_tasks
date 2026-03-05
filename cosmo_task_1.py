import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        monht = input()
        if 0<int(monht)<3 or int(monht) == 12:
            print("Winter")
        elif 2<int(monht)<6:
            print("Spring")
        elif 5<int(monht)<9:
            print("Summer")
        elif 8<int(monht)<12:
            print("Autumn")
        else:
            print("Error")
    except EOFError:
        break