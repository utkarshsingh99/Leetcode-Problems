class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        nz1, nz2 = sum(x == 0 for x in nums1), sum(x == 0 for x in nums2)
        
        if sum1 == sum2:
            if (nz1 == 0 and nz2 > 0) or (nz1 > 0 and nz2 == 0):
                return -1
            else:
                return sum1 + max(nz1, nz2)
        elif (nz1 == 0 and nz2 > 0):
            if sum1 >= sum2 + nz2:
                return sum1
            else:
                return -1
        elif (nz2 == 0 and nz1 > 0):
            if sum2 >= sum1 + nz1:
                return sum2
            else:
                return -1
        elif (nz1 == 0 and nz2 == 0):
            return -1
        else:
            return max(sum1 + nz1, sum2 + nz2)
            
        