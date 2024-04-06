
import re
s = input()
s = re.sub(r'[aeiouyAEIOUY]', '', s)
s = re.sub(r'(?=[^aeiouy])', '.', s)
s = re.sub(r'[B-Z]', lambda x: x.group().lower(), s)

print(s)
