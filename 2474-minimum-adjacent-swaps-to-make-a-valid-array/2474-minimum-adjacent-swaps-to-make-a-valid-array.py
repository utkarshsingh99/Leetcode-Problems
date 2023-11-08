class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        low, high = (-1, float('infinity')), (-1, -1)

        for i in range(len(nums)):
            if low[1] > nums[i]:
                low = (i, nums[i])
            if high[1] <= nums[i]:
                high = (i, nums[i])
        
        li, hi, count = low[0], high[0], 0

        count = li + (len(nums) - 1 - hi)
        # print(li, hi, len(nums))
        if hi < li:
            count -= 1
        return count