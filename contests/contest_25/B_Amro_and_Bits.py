

for _ in range(int(input())):

    num = int(input())

    if num == 1:
        print(3)
        continue

    fisrt_one_pos = None
    first_zero_pos = None

    cpt_ones = 0

    pos = 0
    while num:
        num, r = divmod(num, 2)

        if r == 0 and first_zero_pos is None:
            first_zero_pos = pos

        if r == 1:
            if fisrt_one_pos is None:
                fisrt_one_pos = pos
            cpt_ones += 1

        pos += 1

    if cpt_ones > 1:
        print(2**fisrt_one_pos)
    else:
        print(2**first_zero_pos + 2**fisrt_one_pos)
