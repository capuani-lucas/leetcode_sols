class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # O(s + t) RT

        if len(s) != len(t):
            return False
        
        char_counter_s = {}
        char_counter_t = {}
        
        # O(s)
        # Count chars 
        for i in s:
            if i in char_counter_s:
                char_counter_s[i] = char_counter_s[i] + 1
            else:
                char_counter_s[i] = 1
        
        # O(t)
        # Count chars
        for i in t:
            if i in char_counter_t:
                char_counter_t[i] = char_counter_t[i] + 1
            else:
                char_counter_t[i] = 1

        # If char from one set not found in other = not anagram
        # If # of times char appears not same in other string = not anagram
        for i in char_counter_s:
            if not i in char_counter_t:
                return False
            if char_counter_s[i] != char_counter_t[i]:
                return False
            
        return True