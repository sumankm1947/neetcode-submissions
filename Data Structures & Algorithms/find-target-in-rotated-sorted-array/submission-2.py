class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            print(f"l:{l}")
            print(f"r:{r}")

            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            
            # case 1: if increasing array
            if nums[r] > nums[l]:
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # case 2: there is rotation
            else:
                # subcase 1: mid is in the increasing part - 2 cases
                if nums[mid] >= nums[l]:
                    if target <= nums[mid] and target >= nums[l]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    # subcase 2: mid comes after the smallest element
                    if target <= nums[r] and target >= nums[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1

        
        if target == nums[l]:
            return l
        print(l)
        print(r)
        

        return -1