

for _ in range(int(input())):

    bin_array = list(input())

    cpt = 1
    left = 1

    x = 0
    while left < len(bin_array):

        if bin_array[left] != bin_array[left - 1]:
            cpt += 1

        if bin_array[left] == '1' and bin_array[left - 1] == '0':
            x = 1

        left += 1
    print(cpt-x)
