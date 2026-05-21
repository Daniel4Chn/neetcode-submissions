class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        setOfTriplets = set()
        k = len(nums)-1
        nums = sorted(nums)
        for i in range(len(nums)-2):
            k = len(nums)-1
            j = i+1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0 and (nums[i],nums[j],nums[k]) not in setOfTriplets:
                    setOfTriplets.add((nums[i],nums[j],nums[k]))
                    out.append([nums[i],nums[j],nums[k]])
                    k-=1
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return out
        
