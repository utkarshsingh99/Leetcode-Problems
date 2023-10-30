class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
#         max_i, val = -inf, 0
#         for j in range(len(nums)):
#             max_i = max(max_i, nums[j])
#             for k in range(j + 1, len(nums)):
#                 val = max((max_i - nums[j])*nums[k], val)
                    
#         return val
        
        highest, lowest = -1, -1
        val = 0
        b = set()
        for i in nums:
            for each in b:
                # print(i, each, (each[0] - each[1])*i)
                val = max(val, (each[0] - each[1])*i)
            if highest < i:
                highest = i
                lowest = i
            elif lowest > i:
                lowest = i
            if highest != lowest:
                b.add((highest, lowest))
        return val
        