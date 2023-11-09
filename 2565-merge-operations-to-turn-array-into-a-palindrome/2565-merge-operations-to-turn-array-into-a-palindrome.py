class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        j, ans = n-1, 0
        while i <= j:
            f, l = nums[i], nums[j]
            fn, ln = nums[i+1], nums[j-1]

            if f > l:
                nums[j-1] = l + ln
                ans += 1
                j -= 1
            elif f < l:
                nums[i+1] = f + fn
                ans += 1
                i += 1
            elif f == l:
                i += 1
                j -= 1
        return ans