class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        left = 0 
        longest = 0 

        for _ in range(len(s)):
            while s[_] in seen: 
                seen.remove(s[left])
                left += 1
            
            seen.add(s[_])
            longest = max(longest, _ - left + 1)
        
        return longest 