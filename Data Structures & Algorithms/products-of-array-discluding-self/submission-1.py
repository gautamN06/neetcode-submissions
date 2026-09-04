class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = [1] * len(nums)

        left_ans = 1
        for i in range(len(nums)):
            answer[i] = left_ans 
            left_ans *= nums[i]
        
        right_ans = 1 
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= right_ans
            right_ans *= nums[i]

        return answer 