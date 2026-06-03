class Solution:
    def maxAbsoluteSum(self, nums):
        max_ending = 0
        min_ending = 0

        max_sum = 0
        min_sum = 0

        for num in nums:
            max_ending = max(num, max_ending + num)
            max_sum = max(max_sum, max_ending)

            min_ending = min(num, min_ending + num)
            min_sum = min(min_sum, min_ending)

        return max(max_sum, abs(min_sum))