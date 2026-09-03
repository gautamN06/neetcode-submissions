class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #return a list of the answers that add up to 0 
        result_list = []
        #sort list so computations will be easier with two pointers 
        nums.sort() 

        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l, r = i+1, len(nums)-1

            while l < r: 
                total = nums[i] + nums[l] + nums[r]

                if total > 0: 
                    r-=1 
                elif total < 0: 
                    l += 1
                else: 
                    result_list.append([nums[i], nums[l], nums[r]])
                    l+=1 
                    r-=1 

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return result_list 





