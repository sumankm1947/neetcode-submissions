class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = {}
        for num in nums:
            if num in num_list:
                return True
            else:
                num_list[num] = 0
        return False
        