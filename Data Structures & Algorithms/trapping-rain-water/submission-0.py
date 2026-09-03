class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1 

        left_tallest = 0 
        right_tallest = 0 
        total_water = 0 

        while l < r: 
            if height[r] >= height[l]:

                curr_height = height[l]

                left_tallest = max(left_tallest, curr_height)

                total_water += left_tallest - curr_height 

                l+=1 
            
            else: 
        
                curr_height_right = height[r]

                right_tallest = max(right_tallest, curr_height_right)

                total_water += right_tallest - curr_height_right 

                r -= 1

        return total_water 


            
