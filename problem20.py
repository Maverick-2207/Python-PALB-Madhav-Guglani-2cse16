def trap_rainwater(arr):
    if not arr or len(arr) < 3:
        return 0

    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water


# Example usage
if __name__ == "__main__":
    print(trap_rainwater([3, 0, 2, 0, 4]))          # 7
    print(trap_rainwater([1, 2, 3, 4]))             # 0
    print(trap_rainwater([2, 1, 5, 3, 1, 0, 4]))    # 9
