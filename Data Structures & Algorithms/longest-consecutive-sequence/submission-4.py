class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hashmap = defaultdict(int)
        for num in nums:
            if hashmap[num] != 0:
                continue
            
            length = hashmap[num - 1] + 1 + hashmap[num + 1]
            hashmap[num] = length
            if length > ans:
                ans = length
            hashmap[num - hashmap[num - 1]] = length
            hashmap[num + hashmap[num + 1]] = length
            
        return ans