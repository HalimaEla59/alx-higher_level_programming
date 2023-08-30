#!/usr/bin/python3

class Node:
    """class Node"""

    def __init__(self, data, next_node=None):
        """initialize a node
        args:
           data(int): data of node
           next_node(Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter data of Node"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter data of node"""
        if(not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter next node of Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter next node"""
        if(not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        """initializing"""
        self.__head = None

    def __str__(self):
        """print representation"""
        val = []
        while(self.__head):
            val.append(self.__head.data)
            self.__head = self.__head.next_node
        return("\n".join([str(x) for x in sorted(val)]))

    def sorted_insert(self, value):
        """inserts new Node"""
        newNode = Node(value, self.__head)
        self.__head = newNode
