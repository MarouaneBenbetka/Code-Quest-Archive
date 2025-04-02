from collections import defaultdict


for _ in range(int(input())):
    number = input()
    n = len(number)

    position = defaultdict(list)
    for i, digit in enumerate(number):
        if digit in '0257':
            position[digit].append(i)

    # 00
    option1 = float('inf')
    if len(position['0']) >= 2:
        # xxx0xxx0
        for i in range(len(position['0'])):
            for j in range(i+1, len(position['0'])):
                pos1, pos2 = position['0'][i], position['0'][j]
                option1 = min(option1, n-pos2-1 + pos2-pos1-1)
    else:
        if len(position['0']) == 1:
            option1 = n - 1

    # 50
    option2 = float('inf')
    if len(position['5']) and len(position['0']):
        # xxx5xxx0
        for pos1 in position['5']:
            for pos2 in position['0']:
                if pos2 > pos1:
                    option2 = min(option2, n-pos2-1 + pos2-pos1-1)

    # 25
    option3 = float('inf')
    if len(position['2']) and len(position['5']):
        # xxx2xxx5
        for pos1 in position['2']:
            for pos2 in position['5']:
                if pos2 > pos1:
                    option3 = min(option3, n-pos2-1 + pos2-pos1-1)

    # 75
    option4 = float('inf')
    if len(position['7']) and len(position['5']):
        # xxx7xxx5
        for pos1 in position['7']:
            for pos2 in position['5']:
                if pos2 > pos1:
                    option4 = min(option4, n-pos2-1 + pos2-pos1-1)

    print(min(option1, option2, option3, option4))
