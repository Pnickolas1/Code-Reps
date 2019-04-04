from random import randint
random_numbers = [24, 40, 23, 98, 44, 19, 8, 31, 31, 8, 38, 0, 35, 50, 3,
                   45, 44, 41, 5, 16, 29, 25, 25, 32, 25, 20, 34, 36, 3, 19]

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


class Element:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):

    def __init(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):

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
        """"
        insert a new node at the given position
        assume the first position is "1"
        inserting at position 3 means between
        the 2nd and 3rd elements
        """

        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position -1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element


    def delete(self, value):
        """
        delete the first node with a given value
        :param value:
        :return:
        """

        current = self.head
        previous = None
        while current.next != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next


es1  = Element(1)
es2 = Element(2)
es3 = Element(3)
es4 = Element(4)



ll = LinkedList(es1)

ll.append(es2)
ll.append(es3)



if __name__ == "__main__":
    print(es1, es2, es3, es4)
    print(ll)