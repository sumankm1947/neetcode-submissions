class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ans_per = 1
            for j in range(n):
                if j == i:
                    continue
                else:
                    ans_per *= nums[j]
            
            ans.append(ans_per)
        return ans