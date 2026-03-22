class Solution:
    def moveZeroes(self, nums):
        j = 0
        
        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Fill remaining with zeros
        for i in range(j, len(nums)):
            nums[i] = 0