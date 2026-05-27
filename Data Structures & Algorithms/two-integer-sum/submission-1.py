class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            value = nums[i]
            complement = target - value            
            if complement in hash_map:
                index2 = hash_map[complement]
                ans = [i, index2]
                ans.sort()
                return ans
            hash_map[nums[i]] = i