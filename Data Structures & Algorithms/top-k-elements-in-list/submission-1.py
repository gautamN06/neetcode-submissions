class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_frequent = {}

        for num in nums:
            if num in most_frequent:
                most_frequent[num] += 1
            else: 
                most_frequent[num] = 1
            
        sorted_nums = sorted(
            most_frequent, 
            key=most_frequent.get, 
            reverse=True
        )

        return sorted_nums[:k]