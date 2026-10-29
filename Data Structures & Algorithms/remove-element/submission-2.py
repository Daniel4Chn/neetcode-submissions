class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #the first k elements of nums contain the elements which are not equal to val
    
        swapIndex = len(nums)-1
        numOfSwaps = 0
        i = 0
        while i <= swapIndex:
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[swapIndex]
                nums[swapIndex] = temp
                swapIndex-=1
                numOfSwaps+=1
                continue
            i+=1
        return len(nums)-numOfSwaps
