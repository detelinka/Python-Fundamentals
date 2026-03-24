import re
import sys

text = ''.join(sys.stdin.readlines())      # четем всички редове наведнъж
numbers = re.findall(r'\d+', text)         # всички последователности от цифри
print(' '.join(numbers))                   # отделени с интервал
