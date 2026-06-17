import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        ans = []
        l = 0
        r = 0
        n = len(nums)

        while r < n:
            while d and nums[d[-1]] < nums[r]:
                d.pop()
            
            d.append(r)

            if r >= k - 1:
                ans.append(nums[d[0]])

                l += 1
                if d[0] < l:
                    d.popleft()
            
            r += 1
            
        
        return ans
