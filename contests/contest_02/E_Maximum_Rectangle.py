def max_rectangle_area(s):
    n = len(s)
    # Initialize an array to store the height of the rectangle ending at each position
    height = [0] * n
    max_area = 0

    # Compute the height of the rectangle ending at each position
    for i in range(n):
        if s[i] == '1':
            height[i] = 1
            if i > 0:
                height[i] += height[i - 1]

    # Iterate through each position to calculate the maximum area
    for i in range(n):
        width = 1
        # Check the area of rectangle with bottom-right corner at position (i, j)
        for j in range(i, -1, -1):
            # Update width to the minimum height among all positions from i to j
            width = min(width, height[j])
            # Calculate the area of the rectangle and update max_area if greater
            max_area = max(max_area, width * (i - j + 1))

    return max_area


# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the binary string
    s = input()
    # Calculate and print the maximum area of a rectangle consisting only of ones
    print(max_rectangle_area(s))
