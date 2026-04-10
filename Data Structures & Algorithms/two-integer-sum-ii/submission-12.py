class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers at start and end of sorted array
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-based indices per problem constraints
                return [left + 1, right + 1]
            
            elif current_sum < target:
                # Sum too small: move left pointer to increase value
                left += 1
            else:
                # Sum too large: move right pointer to decrease value
                right -= 1