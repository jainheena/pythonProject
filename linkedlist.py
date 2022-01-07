

import math
import os
import random
import re
import sys


class NodeForSinglyLinkedList:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = NodeForSinglyLinkedList(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

            self.tail = node

