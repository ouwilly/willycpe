import sys

keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
#ketboard="`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

text = sys.stdin.read()

for ch in text:
    if ch == " " or ch == "\n":
        print(ch, end="")
    else:
        index = keyboard.find(ch)
        print(keyboard[index - 2], end="")