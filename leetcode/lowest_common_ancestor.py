

"""
given a tree, two nodes within the tree, return its lowest common ancestor

"""


class Solution:    
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(root, p, q ):
        
        def LCA(node, p, q):

            if node == None:
                return None

            # if node is p or q then return that node to the node
            if node.val == p.val or node.val == q.val:
                return node

            # finding left and right sub tree
            left_part = LCA(node.left, p, q)
            right_part = LCA(node.right, p, q)

            # if both left and right subtree are none then return node to the parent 
            if left_part != None and right_part != None:
                return node

            # if one sub tree is null and one sub tree is not null
            else:
                return left_part if left_part else right_part

        return LCA(root, p, q)


def lowestCommonAncestor(root, p, q):

    if not root: return None
	
    if root == p or root == q: return root
	
    l = lowestCommonAncestor(root.left, p, q)
    r = lowestCommonAncestor(root.right, p, q)
	
    if l and r:
        return root
    else:
        return l if l else r

   
