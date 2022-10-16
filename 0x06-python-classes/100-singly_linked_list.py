#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node -> private data & next_node
Defines class SinglyLinkedList -> private head & public sorted_insert
"""


class Node:
    """
    class Node def

    Args:
        data (int): private
        next_node : private; can be None or Node object

    Functions:
        __init__(self, data, next_node=None)
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    """

    def __init__(self, data, next_node=None):
        """
        Init node

        Attributes:
            data (int): private
            next_node : private; can be None or Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        Getter

        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter

        Args:
            value: set data to value if int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"
        Getter

        Return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value: set next_node if-> value is next_node or None
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList def

    Args:
        head: private

    Functions:
        __init__(self)
        sorted_insert(self, value)
    """

    def __init__(self):
        """
        Init -> singly linked list

        Attributes:
            head: private
        """
        self.__head = None

    def __str__(self):
        """
        Str -> singly linked list needed to print
        """
        string = ""
        tp = self.__head
        while tp is not None:
            string += str(tp.data)
            tp = tp.next_node
            if tp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        Insert new_nodes -> sorted singly linked list

        Args:
        value: int data for node
        """
        nW = Node(value)
        if self.__head is None:
            self.__head = nW
            return

        tp = self.__head
        if nW.data < tp.data:
            nW.next_node = self.__head
            self.__head = nW
            return

        while (tp.next_node is not None) and (nW.data > tp.next_node.data):
            tp = tp.next_node
        nW.next_node = tp.next_node
        tp.next_node = nW
        return
