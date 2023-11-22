#!/usr/bin/python3
"""Creating a class of singly linked list."""


class Node:
    """Defining the class of Node."""

    def __init__(self, data, next_node=None):
        """the function of the initialisatio.

        Args:
            data (int): the variable passed of the nodee.
            next_node (Node): node pointing to the nest list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """setting the data to the variable."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """passing the data of linked listt."""

    def __init__(self):
        """the initializer of the singly."""
        self.__head = None

    def sorted_insert(self, value):
        """Function to insert data to the listt.

        passing the value at an index.

        Args:
            value (Node): the value passed.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """printing the linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
