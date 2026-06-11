class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        n = len(s)

        ans = 0
        for c in charSet:
            l = 0
            count = 0

            for r in range(n):
                if s[r] == c:
                    count += 1
                
                k_tillnow = r - l - count + 1
                while k_tillnow > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                    k_tillnow = r - l - count + 1
                
                ans = max(r - l + 1, ans)
        
        return ans
