class Solution:
    def isSpeedAcceptable(self, piles: List[int], speed: int, h: int) -> bool:
        total_hrs_taken = 0
        if speed == 0:
            return False
        for pile in piles:
            if speed > pile:
                total_hrs_taken += 1
            else:
                total_hrs_taken += math.ceil(pile / speed)            
        return total_hrs_taken <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = 10 ** 9
        l = 0
        isFoundOneAns = False
        n = len(piles)
        ans = 10**9

        while l <= r:
            mid = (r + l) // 2
            # print(f"l: {l}, r: {r}")
            if self.isSpeedAcceptable(piles, mid, h):
                isFoundOneAns = True
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
            
            # print()
        
        return ans
