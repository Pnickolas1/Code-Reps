

""""


All BSTS should be have ability to

Average Case:
    Time: O(log n)      (for all three operations below), n is the number of nodes in the BST
    Space: O(log n)     (if implemented recursively)

Worst Case:
    Time: O(n)
    Space: O(n)

 - Insert


 - Search'
 - Delete


When Deleting **
you replace the node to be deleted, you replace it the SMALLEST VALUE IN THE RIGHT SUBTREE
of that node, grab the left most value in the right subtree



"""

class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        implemented iteratively, iterative solutions are better


        # Average O(log N) time || O(1) space
        # Worst O(n) time || O(1) space
        :param value:
        :return:
        """
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self


    def contains(self, value):
        """
        # Average O(log N) time || O(1) space
        # Worst O(n) time || O(1) space

        :param value:
        :return:
        """
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def remove(self, value, parentNode = None):
        """
        # Average O(log N) time || O(1) space
        # Worst O(n) time || O(1) space

        :param value:
        :param parentNode:
        :return:
        """
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right

            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right._getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                # because the root doesnt have a parent node
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        """
                        effectively deleting the BST
                        """
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break

        return self


    def _getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value




























