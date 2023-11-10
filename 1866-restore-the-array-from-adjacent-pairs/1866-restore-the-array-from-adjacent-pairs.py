from collections import defaultdict 
class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        for a, b in adjacentPairs:
            d[a].append(b)
            d[b].append(a)
        
        start = None
        for each in d.keys():
            if len(d[each]) < 2:
                start = each
                break
        
        ans = [start, d[start][0]]
        key, val = start, d[start][0]
        while True:
            
            prev = key
            key = val
            if len(d[key]) == 1:
                # ans.append(d[key][0])
                break
            val = d[key][0] if d[key][0] != prev else d[key][1]



            # prev = start
            # print(ans)
            # if d[start][0] == prev:
            #     if len(d[start]) == 1:
            #         break
            #     start = d[start][1]
            # else:
            #     start = d[start][0]
            
            ans.append(val)
        
        return ans