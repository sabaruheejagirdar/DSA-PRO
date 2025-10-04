# Time Complexity: O(n)
# Space Complexity: O(n)

def trap(height):
    n = len(height)
    if n == 0:
        return 0

    maxLeft = [0] * n
    maxRight = [0] * n
    water = 0

    # Build maxLeft
    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i - 1], height[i - 1])

    # Build maxRight
    for i in range(n - 2, -1, -1):
        maxRight[i] = max(maxRight[i + 1], height[i + 1])

    # Calculate trapped water
    for i in range(n):
        minLR = min(maxLeft[i], maxRight[i])
        if minLR > height[i]:
            water += minLR - height[i]

    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
output = trap(height)
print(output)