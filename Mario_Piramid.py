high = int(input("How high the Mario Piramid should be: "))
for line in range(high):
    print (" " * (high-line-1) + "#" * (2 * line +1))