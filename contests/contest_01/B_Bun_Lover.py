
def sum_of_series(n):
    # Calculate the number of terms
    num_terms = float((n + 2) // 2)

    # Calculate the sum using the formula for the sum of an arithmetic series
    first_term = 4 * n
    last_term = 4
    series_sum = num_terms * (first_term + last_term) / 2

    return series_sum


def chocolate_length(t, n):

    length = 2 - n % 2  # Starting adjustment based on whether n is odd or even
    for i in range(n, 0, -2):
        length += 4 * i

    print(int(length))


def chocolate_length_sum_formula(n):
    k = (n + n % 2) / 2
    a = 4 * n
    d = -8
    length = (k / 2) * (2 * a + (k - 1) * d)
    length += 2 - n % 2
    print(int(length))


# Example Input
t = int(input())

for _ in range(t):
    n = int(input())
    chocolate_length_sum_formula(n)
