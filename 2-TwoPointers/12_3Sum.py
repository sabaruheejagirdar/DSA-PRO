# Time Complexity: O(n^2)
# Space Complexity: O(1)

def threeSum(nums):
    # res = []
    res = set()
    nums.sort()
    
    for i in range(len(nums)-2):
        curr = nums[i]
        left = i+1
        right = len(nums) -1
        while left < right:
            l = nums[left]
            r = nums[right]
            currSum = curr + l + r

            if currSum == 0:
                sumSet = (curr, nums[left], nums[right])
                res.add(sumSet)
                left += 1
            elif currSum < 0:
                left += 1
            elif currSum > 0:
                right -= 1
            
    
    return [list(triplet) for triplet in res]

input = [-1,0,1,2,-1,-4]
output = threeSum(input)
print(output)