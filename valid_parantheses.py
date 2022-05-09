class Solution:
    def isValid(self, s: str) -> bool:
        
        # O(n) RT
        
        # If string list not even
        if len(s) % 2 != 0:
            return False
    
        # Dict of openings with respective closings
        openings = {'(': ')', '{': '}', '[': ']'}
        
        # Stack DSA
        char_stack = []
        
        # Track amounts
        num_of_opening = 0
        num_of_closing = 0
        
        for i in s:
            # i is opening bracket
            if i in openings:
                # Push to stack
                char_stack.append(i)
                num_of_opening += 1
            # i is closing bracket
            else:
                # If there are no opening brackets expression not valid
                if len(char_stack) == 0:
                    return False
                num_of_closing += 1
                # Get most recent added opening 
                type_opening = char_stack.pop()
                # If the closing bracket does not match opening associated bracket 
                if i != openings[type_opening]:
                    return False
        return num_of_opening == num_of_closing