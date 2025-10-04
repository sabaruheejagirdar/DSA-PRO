# Time Complexity: O(n)
# Space Complexity: O(1)

def maxArea(height):
    l = 0
    r = len(height) - 1
    maxArea = 0
    while l < r:
        length = r - l
        width = min(height[l], height[r])
        area =  length * width

        maxArea = max(area, maxArea)

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l+=1

    return maxArea

height = [1,8,6,2,5,4,8,3,7]
output = maxArea(height)
print(output)