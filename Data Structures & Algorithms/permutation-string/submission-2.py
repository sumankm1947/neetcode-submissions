class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        charats1 = [0] * 26
        charats2 = [0] * 26

        for s in s1:
            charats1[ord(s) - ord('a')] += 1
        
        for i in range(n1):
            charats2[ord(s2[i]) - ord('a')] += 1
        
        l = 0
        r = n1
        while r < n2:
            if charats1 == charats2:
                return True
            else:
                charats2[ord(s2[l]) - ord('a')] -= 1
                charats2[ord(s2[r]) - ord('a')] += 1
                l += 1
                r += 1
        if charats1 == charats2:
            return True
        return False
