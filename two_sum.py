class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        used = {}
        
        # O(n) running time
        for i, v in enumerate (nums):
            needed = target - nums[i] # check hashtable for this value
            try:
                val = used[needed] # check the hashtable
                return [i, val] # index found return
            except:
                pass 
            used[v] = i # add to table after so no duplicates
                