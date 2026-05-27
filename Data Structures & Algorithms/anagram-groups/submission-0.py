class Solution:
    def giveCharList(self, string: str) -> Tuple[int]:
        hash_map = [0] * 26
        for char in string:
            hash_map[ord(char) - ord('a')] += 1
        return tuple(hash_map)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for word in strs:
            key = self.giveCharList(word)
            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]
    
        ans = []
        for key, value in hash_map.items():
            ans.append(value)

        print(ans)
        return ans
