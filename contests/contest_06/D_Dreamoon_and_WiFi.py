
from collections import Counter
import math

original = Counter(input())
wifi = Counter(input())

plus_left = max(original['+'] - wifi['+'], 0) + \
    abs(min(0, original['-'] - wifi['-']))

minus_left = max(original['-'] - wifi['-'], 0) + \
    abs(min(0, original['+'] - wifi['+']))

possible_cases = wifi['?']
if plus_left == 0 and minus_left == 0:
    print(1)
else:
    if possible_cases < (plus_left + minus_left):
        print(0)
    else:
        print(math.factorial(possible_cases)//(math.factorial(plus_left)
              * math.factorial(minus_left))/2**possible_cases)
