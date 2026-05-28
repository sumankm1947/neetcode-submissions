class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_cal = [1] * n
        postfix_cal = [1] * n
        prefix_cal[0] = nums[0]
        postfix_cal[n-1] = nums[n-1]
        ans = [1] * n

        for i in range(1, n):
            prefix_cal[i] = prefix_cal[i - 1] * nums[i]
        for i in range(n-2, 0, -1):
            postfix_cal[i] = postfix_cal[i + 1] * nums[i]
        
        ans[0] = postfix_cal[1]
        ans[n - 1] = prefix_cal[n - 2]
        for i in range(1, n - 1):
            ans[i] = prefix_cal[i - 1] * postfix_cal[i + 1]
        
            
        return ans