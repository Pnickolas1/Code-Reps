

"""

  N ary traversals
  preOrder
  InOrder







"""
from collections import deque

def nAry_preorder(root):
    """

    Input: root = [1,null,3,2,4,null,5,6]
    Output: [1,3,5,6,2,4]
    
    [1,3,2,4,5,6]
    """
    if root is None:
        return []
    
    stack, = [root]
    output = []
    while stack:
        root = stack.pop()
        output.append(root.val)
        stack.extend(root.children[::-1])
            
    return output


def nAry_postOrder(root):
    if root is None:
        return []
    
    stack = [root]
    res = []
    while stack:
        root = stack.pop()
        if root is not None:
            res.append(root.val)
        for c in root.children:
            stack.append(c)
            
    return res[::-1]















def maxDepth(root):
    
    """
        dfs 
        recursion
    """

    if root is None: 
        return 0 
    elif root.children == []:
        return 1
    else: 
        height = [maxDepth(c) for c in root.children]
        return max(height) + 1 

class WrappableInt:
        def __init__(self, x):
            self.value = x
        def getValue(self):
            return self.value
        def increment(self):
            self.value += 1

class Codec:
    
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serializedList = []
        self._serializeHelper(root, serializedList, WrappableInt(1), None)
        return "".join(serializedList)
    
    def _serializeHelper(self, root, serializedList, identity, parentId):
        if not root:
            return
        
        # Own identity
        serializedList.append(chr(identity.getValue() + 48))
        
        # Actual value
        serializedList.append(chr(root.val + 48))
        
        # Parent's identity
        serializedList.append(chr(parentId + 48) if parentId else 'N')
        
        parentId = identity.getValue()
        for child in root.children:
            identity.increment()
            self._serializeHelper(child, serializedList, identity, parentId)
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        
        if not data:
            return None
        
        return self._deserializeHelper(data)
        
    def _deserializeHelper(self, data):
        
        nodesAndParents = {}
        for i in range(0, len(data), 3):
            identity = ord(data[i]) - 48
            orgValue = ord(data[i + 1]) - 48
            parentId = ord(data[i + 2]) - 48
            nodesAndParents[identity] = (parentId, Node(orgValue, []))
            
        for i in range(3, len(data), 3):
            
            # Current node
            identity = ord(data[i]) - 48
            node = nodesAndParents[identity][1]
            
            # Parent node
            parentId = ord(data[i + 2]) - 48
            parentNode = nodesAndParents[parentId][1]
            
            # Attach!
            parentNode.children.append(node)
            
        return nodesAndParents[ord(data[0]) - 48][1]    