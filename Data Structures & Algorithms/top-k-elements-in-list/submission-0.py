class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        
        sorted_hash_map = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))        
        print(sorted_hash_map)
        i = 0
        ans = []
        for key, value in sorted_hash_map.items():
            if i ==k:
                return ans
            ans.append(key)
            i += 1
        return ans
