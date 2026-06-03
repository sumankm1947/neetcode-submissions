class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        premax = [0] * n
        postmax = [0] * n
        premax[0] = height[0]
        postmax[n - 1] = height[n - 1]


        for i in range(1, n):
            pre = max(height[i], premax[i - 1])
            premax[i] = pre
        
        for j in range(n - 2, -1, -1):
            post = max(height[j], postmax[j + 1])
            postmax[j] = post
        
        print(premax)
        print(postmax)
        ans = 0

        for i in range(n):
            minheight = min(premax[i], postmax[i])
            if minheight > height[i]:
                ans += minheight - height[i]
        
        return ans
