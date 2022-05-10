class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # O(n) RT. Kadane's algorithm
        
        if len(nums) == 1:
            return nums[0]
        
        max_sum = nums[0] - 1
        current_sum = 0

        for i in nums:
            # Start counting from this part of subarray
            # or continue counting if it increases the sum
            current_sum = max(i, i + current_sum)
            # update new max sum found
            if current_sum > max_sum:
                max_sum = current_sum
                
        
        return max_sum
        
            
        