class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set()

        for _ in nums:
            if _ in unique_num:
                return True 
            unique_num.add(_)
        return False 