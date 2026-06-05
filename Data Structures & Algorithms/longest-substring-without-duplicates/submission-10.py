class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable = {}
        n = len(s)
        currindex = 0
        ans = 0
        cnt = 0
        startindex = 0
        if n == 1:
            return 1

        while currindex < n:
            print(str(startindex) + " " + str(currindex))
            print(s[startindex: currindex + 1])
            if s[currindex] in hashtable and hashtable[s[currindex]] == 1:
                # cnt -= 1
                ans = max(ans, cnt - 1)
                while startindex <= currindex and s[startindex] != s[currindex]:
                    hashtable[s[startindex]] -= 1
                    startindex += 1
                    cnt -= 1
                hashtable[s[startindex]] = 1
                startindex += 1
            else:
                hashtable[s[currindex]] = 1
                cnt += 1
                ans = max(ans, cnt)
            
            currindex += 1
        
        ans = max(ans, cnt)
        return ans
                