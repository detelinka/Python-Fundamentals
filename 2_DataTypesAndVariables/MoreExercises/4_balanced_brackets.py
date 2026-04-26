n = int(input())

balanced = True
open_bracket = False

for _ in range(n):
    text = input()
    if text == '(':
        if open_bracket:
            balanced = False
            break
        open_bracket = True
    elif text == ')':
        if not open_bracket:
            balanced = False
            break
        open_bracket = False

if balanced and not open_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")