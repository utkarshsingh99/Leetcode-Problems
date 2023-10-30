class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = [0]*32
        
        for each in nums:
            n, ind = each, 31
            while n > 0:
                if n & 1:
                    bits[ind] += 1
                ind -= 1
                n = n // 2
        
        ans, step = 0, 0
        for i in range(31, -1, -1):
            if bits[i] >= k:
                ans += 2 ** step
            step += 1
        return ans
        