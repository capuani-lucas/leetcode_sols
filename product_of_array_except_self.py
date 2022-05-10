class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # O(n)
        
        # Fill array with 1s
        output_array = [1 for i in nums]
        
        curr = 1
        # Sweep left to right
        # output[i] = product of all BEFORE it
        for i in range(len(nums)):
            output_array[i] = curr
            curr *= nums[i]
            
        curr = 1
        # Sweep right to left
        # output[i] = product of all AFTER it * before it
        for i in range(len(nums) - 1, -1, -1):
            output_array[i] *= curr
            curr *= nums[i]
            
        return output_array