# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def trav(root):
            if root is None:
                # (avg_node_count, total, count)
                return (0, 0, 0)
            tot, count = root.val, 1

            left = trav(root.left)
            right = trav(root.right)

            tot += left[1] + right[1]
            count += left[2] + right[2]

            avg_node_count = left[0] + right[0]

            if root.val == int(tot / count):
                avg_node_count += 1
            
            return (avg_node_count, tot, count)
        
        return trav(root)[0]
        