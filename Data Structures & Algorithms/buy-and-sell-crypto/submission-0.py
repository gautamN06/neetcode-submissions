class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_prof = 0

        for _ in prices: 
            min_price = min(min_price, _)
            max_prof = max(max_prof, _ - min_price)

        return max_prof