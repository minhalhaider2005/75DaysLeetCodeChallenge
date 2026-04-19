class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # agar leaf node hai
        if not root.left and not root.right:
            return targetSum == root.val
        
        # left ya right me check karo
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))