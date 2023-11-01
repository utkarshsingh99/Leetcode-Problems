# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = []
        def traverse(root):
            if root is None:
                return None
            d.append(root.val)

            traverse(root.left)
            traverse(root.right)  
            return None
        traverse(root)
        dd = Counter(d)
        if len(dd) == 0:
            return []
        high = dd.most_common(1)[0][1]
        ans = []
        # print('HH: ', high)
        for i, v in dd.items():
            # print(v)
            if v == high:
                ans.append(i)
        return ans
        