# Time Complexity: O()
# Space Complexity: O()

def twoSum(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:
        currSum = numbers[left] + numbers[right]
        if currSum == target:
            return [left+1, right+1]
        
        elif currSum < target:
            left += 1
        elif currSum > target:
            right -= 1
    
    return 
        

input = [4,7,9,10]
target = 13
output = twoSum(input, target)
print(output)