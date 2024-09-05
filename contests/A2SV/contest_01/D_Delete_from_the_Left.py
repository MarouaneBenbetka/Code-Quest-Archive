

a = input()
b = input()


def min_moves_to_equal_strings(s, t):
    l1 = len(s)
    l2 = len(t)
    len_total = l1 + l2
    c = 0

    if s[l1-1] != t[l2-1]:
        return len_total
    else:
        l1 -= 1
        l2 -= 1
        while l1 >= 0 and l2 >= 0:
            if s[l1] == t[l2]:
                c += 1
                l1 -= 1
                l2 -= 1
            else:
                break
        return len_total - (c * 2)


print(min_moves_to_equal_strings(a, b))
