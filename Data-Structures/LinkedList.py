

class Element(object):
    """
    use __init__ to initialize a new Element
    an Element has a value associated to it, could be anything a string, number, etc &
    it has a variable that points to the next element in the linked list
    """

    def __init__(self, value):
      self.value = value
      self.next = None


class LinkedList(object):
    """
    A LinkedList is something that has a head Element, which is the first element in the list
    if we establish a new linked list without a head, it will default to None
    """

    def __init__(self, head= None):
        self.head = head

    def append(self, new_element):
        """
        method will add a new Element to the end of the LinkedList

        if the LinkedList already has a head, iterate through the next reference in every Element until you
        reach the end of the list, set next for the end of the list to be the new_element

        If there is not head already, you should just assign new_element to it and do nothing else
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """
        Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list
        """
        counter = 1
        current = self.head
        if position < 1:
            return None

        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        """
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                previous = current
                current = current.next
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

    def delete(self, value):
        """
        Delete the first node with a given value
        """
        current = self.head
        previous = None
        while current.value != value and current.next:
          previous = current
          current = current.next
        if current.value == value:
          if previous:
              previous.next = current.next
          else:
              self.head = current.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


print (e1, e2)



