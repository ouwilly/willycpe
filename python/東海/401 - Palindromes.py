# https://onlinejudge.org/external/4/401.pdf
import sys

m = {
    "A":"A", "E":"3", "H":"H", "I":"I", "J":"L",
    "L":"J", "M":"M", "O":"O", "S":"2", "T":"T",
    "U":"U", "V":"V", "W":"W", "X":"X", "Y":"Y",
    "Z":"5", "1":"1", "2":"S", "3":"E", "5":"Z", "8":"8"
}

for s in sys.stdin.read().split():
    p = s == s[::-1]
    r = ""

    for ch in s[::-1]:
        if ch in m:
            r += m[ch]
        else:
            r += "?"

    mirror = s == r

    if p and mirror:
        print(s, "-- is a mirrored palindrome.")
    elif p:
        print(s, "-- is a regular palindrome.")
    elif mirror:
        print(s, "-- is a mirrored string.")
    else:
        print(s, "-- is not a palindrome.")

    print()