def min_moves_to_make_equal(s, t):
    # Reverse both strings to compare their suffixes
    s_reversed = s[::-1]
    t_reversed = t[::-1]

    # Initialize the length of the longest common suffix
    common_suffix_length = 0

    # Compare the characters from the beginning of the reversed strings
    while common_suffix_length < min(len(s), len(t)) and s_reversed[common_suffix_length] == t_reversed[common_suffix_length]:
        common_suffix_length += 1

    # Calculate the minimum number of moves required
    moves_required = (len(s) + len(t)) - 2 * common_suffix_length
    return moves_required


# Example usage
s = input()
t = input()
print(min_moves_to_make_equal(s, t))
