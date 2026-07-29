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
                # case1: mid is maximum in l, mid, r -> in this case min is in the right
                if nums[mid] > nums[l]:
                    l = mid + 1
                # case2: mid is minimum in l, mid, r -> in this case min is in the left
                # but mid can also be minimum -> so check once.
                elif nums[mid] < nums[r]:
                    ans = min(ans, nums[mid])
                    r = mid - 1
                
                # last case mid == l -> which signifies there are only 2 element.
                # check min once and increase l
                else:
                    ans = min(ans, nums[mid])
                    l = mid + 1

        
        if l == r:
            ans = min(ans, nums[l])
        

        return ans
        