class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        print(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] > 0:
                break

            j = i + 1
            k = n - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    # if [nums[i], nums[j], nums[k]] not in ans:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1

        return ans


