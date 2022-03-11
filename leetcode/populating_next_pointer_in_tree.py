import collections


def connect_pointers(root):

    if not root:
        return root
    queue = collections.deque([root])

    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            
            if i < size - 1:
                node.next = queue[0]
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
    return root
