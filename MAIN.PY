# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        # Uncomment one of the following methods to use
        return self.preorderTraversalRecursive(root)
        # return self.preorderTraversalIterative(root)

    def preorderTraversalRecursive(self, root: TreeNode) -> list:
        result = []
        
        def traverse(node):
            if node:
                result.append(node.val)  # Visit the root
                traverse(node.left)       # Visit left subtree
                traverse(node.right)      # Visit right subtree
        
        traverse(root)
        return result

    def preorderTraversalIterative(self, root: TreeNode) -> list:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)  # Visit the root
            if node.right:            # Push right child to stack
                stack.append(node.right)
            if node.left:             # Push left child to stack
                stack.append(node.left)
        
        return result

# Test cases
def test_solution():
    solution = Solution()
    
    # Test case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2, TreeNode(3))
    print(solution.preorderTraversal(root1))  # Expected output: [1, 2, 3]

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3, TreeNode(8), TreeNode(9))
    root2.left.right = TreeNode(5, TreeNode(6), TreeNode(7))
    print(solution.preorderTraversal(root2))  # Expected output: [1, 2, 5, 6, 7, 3, 8, 9]

    # Test case 3: Empty tree
    print(solution.preorderTraversal(None))     # Expected output: []

    # Test case 4: Single node
    root4 = TreeNode(1)
    print(solution.preorderTraversal(root4))  # Expected output: [1]

# Run the tests
test_solution()
