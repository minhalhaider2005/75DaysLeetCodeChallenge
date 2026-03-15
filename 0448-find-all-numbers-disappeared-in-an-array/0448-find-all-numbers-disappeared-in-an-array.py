class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
       
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        return [i + 1 for i, val in enumerate(nums) if val > 0]