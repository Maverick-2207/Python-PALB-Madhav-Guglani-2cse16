def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find entrance to cycle
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Example usage
if __name__ == "__main__":
    print(findDuplicate([1, 3, 4, 2, 2]))  # Output: 2
    print(findDuplicate([3, 1, 3, 4, 2]))  # Output: 3
    print(findDuplicate([3, 3, 3, 3, 3]))  # Output: 3
