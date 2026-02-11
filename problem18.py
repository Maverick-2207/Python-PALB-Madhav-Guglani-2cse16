def is_subset(a, b):
    # Create frequency map of elements in a
    freq = {}

    for num in a:
        freq[num] = freq.get(num, 0) + 1

    # Check each element of b
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1

    return True


# Example usage
if __name__ == "__main__":
    print(is_subset(
        [11, 7, 1, 13, 21, 3, 7, 3],
        [11, 3, 7, 1, 7]
    ))  # True

    print(is_subset(
        [1, 2, 3, 4, 4, 5, 6],
        [1, 2, 4]
    ))  # True

    print(is_subset(
        [10, 5, 2, 23, 19],
        [19, 5, 3]
    ))  # False
