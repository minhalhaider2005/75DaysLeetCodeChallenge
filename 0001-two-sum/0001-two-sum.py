class Solution:
    def twoSum(self, numbers, target):
        number_map = {}

        for i, num in enumerate(numbers):
            complement = target - num

            if complement in number_map:
                return [number_map[complement], i]

            number_map[num] = i
            