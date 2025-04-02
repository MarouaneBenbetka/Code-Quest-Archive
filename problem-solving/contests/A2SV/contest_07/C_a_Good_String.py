
def c_good_string(n, s, a='a'):

    if n == 1:
        return int(s != a)

    m = n//2

    s1 = s[:m]

    s2 = s[m:]

    cpt_s1 = m - s1.count(a)
    cpt_s2 = m - s2.count(a)

    return min(cpt_s1 + c_good_string(m, s2, chr(ord(a)+1)), cpt_s2 + c_good_string(m, s1, chr(ord(a)+1)))


for _ in range(int(input())):
    n = int(input())
    s = input()

    print(c_good_string(n, s))
