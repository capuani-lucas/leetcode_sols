class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # O(n) RT
        # Only need information once. Choose one loop.
        # We are only progressing forward. Must buy before selling
        
        # Start with index 0 as lowest
        lowest = prices[0]
        # Base is max profit is zero
        max_profit = 0
        
        for i in prices:
            # If element is lowest found in list so far
            if i < lowest:
                lowest = i
            
            # i - lowest will be zero if the lowest is the current element so results will not be skewed
            # check if max profit found so far
            if i - lowest > max_profit:
                max_profit = i - lowest
        
        return max_profit