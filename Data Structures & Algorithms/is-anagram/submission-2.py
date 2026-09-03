class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #can't be anagrams if diff num of letters 
        if len(s) != len(t):
            return False 
        
        return sorted(t) == sorted(s)