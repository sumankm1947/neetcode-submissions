class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        ans = nums[0]

        while l < r:
            mid = (r + l) // 2
            if nums[l] < nums[r]:
                # it is in ascending order
                # so min will be l
                ans = min(nums[l], ans)
                break
            else:
                # minimum is in between
                if nums[mid] > nums[l]:
                    l = mid + 1
                elif nums[mid] < nums[r]:
                    ans = min(ans, nums[mid])
                    r = mid - 1
                else:
                    ans = min(ans, nums[mid])
                    l = mid + 1

        
        if l == r:
            ans = min(ans, nums[l])
        

        return ans
        