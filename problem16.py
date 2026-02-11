def merge(intervals):
    if not intervals:
        return []

    # Sort intervals based on starting time
    intervals.sort(key=lambda x: x[0])

    merged = []
    current = intervals[0]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= current[1]:
            # Overlapping intervals → merge
            current[1] = max(current[1], intervals[i][1])
        else:
            # No overlap → push current and move to next
            merged.append(current)
            current = intervals[i]

    merged.append(current)
    return merged


# Example usage
if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
    print(merge([[1,4],[4,5]]))
    print(merge([[4,7],[1,4]]))
