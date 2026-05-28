import sys

text = sys.stdin.read()

left = True

for ch in text:
    if ch == '"':
        if left:
            print("``", end="")
        else:
            print("''", end="")
        left = not left
    else:
        print(ch, end="")