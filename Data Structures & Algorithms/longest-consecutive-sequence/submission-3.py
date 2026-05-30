class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1

        nums = sorted(nums)
        print(nums)
        index = 1
        count = 1
        while index < n:
            if nums[index] == nums[index - 1]:
                pass
            elif nums[index] == nums[index - 1] + 1:
                count += 1
            else:
                if count > ans:
                    ans = count
                count = 1
            index += 1
        if count > ans:
            ans = count

        return ans

        




        return ans