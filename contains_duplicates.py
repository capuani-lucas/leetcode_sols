class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # O(n) RT to convert list to set
        # Set will have unique keys

        # If length decreases, then there were duplicates in the list
        if len(nums) != len(set(nums)):
            return True
        return False
    
        # or
        # previous_elements = {}
        # for element in nums:
        #     if element in previous_elements:
        #         return True
        #     previous_elements[element] = 1
        # return False