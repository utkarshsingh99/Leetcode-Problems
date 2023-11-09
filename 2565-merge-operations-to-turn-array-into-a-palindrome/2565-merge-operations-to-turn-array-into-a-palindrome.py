class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        ans = 0
        while i <= n//2:
            f, l = nums[i], nums[n-1-i]

            if f > l:
                nums[n-1-i] = l + nums[n-2-i]
                nums.pop(n-2-i)
                ans += 1
            elif f < l:
                nums[i] = f + nums[i+1]
                nums.pop(i+1)
                ans += 1
            n = len(nums)
            if f == l:
                i += 1
        return ans