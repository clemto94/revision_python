import sys
import math
from contextlib import redirect_stdout
def translate(text):
    # Write your code here
    # To debug: print ("Debug messages...", file=sys.stderr, flush=True)
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(text)):
        if text[i] in vowels:
            if i != 0 and text[i - 1] in vowels:
                result.append(text[i])
            else:
                result += ["av", text[i]]
        else:
            result.append(text[i])
        return "".join(result)
    return None


# Ignore and do not change the code below
def main():
# pylint: disable = C, W
    text = input()
    with redirect_stdout(sys.stderr):
        javanais = translate(text)
    print(javanais)
if __name__ == "__main__":
    main()