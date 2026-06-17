class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        if n1 < n2:
            return ""
        # if n1 == n2:
        #     if s == t:
        #         return t
        #     else:
        #         return ""

        hash_map = defaultdict(int)
        for c in t:
            hash_map[c] += 1

        i = 0
        j = 0
        minlength = n1
        minStartPoint = i
        counter = n2
        isfound = False

        while j < n1:
            hash_map[s[j]] -= 1

            if hash_map[s[j]] >= 0:
                counter -= 1
            j += 1
            
            while counter == 0:
                isfound = True
                if j - i < minlength:
                    minStartPoint = i
                    minlength = j - i

                hash_map[s[i]] += 1
                if hash_map[s[i]] > 0:
                    counter += 1
                i += 1

                    
        if isfound:
            return s[minStartPoint : minStartPoint + minlength]
        return ""




