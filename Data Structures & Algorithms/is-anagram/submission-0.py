class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table = [0] * 26
        if len(s) != len(t):
            return False

        for char in s:
            hash_table[ord(char) - ord('a')] += 1
        for char in t:
            hash_table[ord(char) - ord('a')] -= 1

        for val in hash_table:
            if val != 0:
                return False
        return True
        