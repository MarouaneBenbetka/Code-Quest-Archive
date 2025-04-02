s = input()
buf = ''


ss = s.split()
live = ''
n = len(ss)

i = 0
while i < n:
    if ss[i] == 'Ctrl':
        if ss[i+2] == 'C':
            buffer = live
            i += 3
        elif ss[i+2] == 'X':
            buffer = live
            live = ''
            i += 3
        elif ss[i+2] == 'V':
            live += buffer
            i += 3
    else:
        live += ss[i] + ' '
        i += 1
print(live)
