class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        j, ans = n-1, 0
        while i <= j:
            f, l = nums[i], nums[j]

            if f > l:
                nums[j-1] = l + nums[j-1]
                # nums.pop(n-2-i)
                ans += 1
                j -= 1
            elif f < l:
                nums[i+1] = f + nums[i+1]
                # nums.pop(i+1)
                ans += 1
                i += 1
            # n = len(nums)
            elif f == l:
                i += 1
                j -= 1
        return ans