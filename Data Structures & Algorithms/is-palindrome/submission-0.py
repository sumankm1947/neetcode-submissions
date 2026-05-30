class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        s = s.replace(' ', '').lower()
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1


        return True