
# https://www.hackerrank.com/challenges/countingsort1/problem

import os
fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

result = [0]*100

for item in arr:
    result[item] += 1

fptr.write(' '.join(map(str, result)))
fptr.write('\n')

fptr.close()
