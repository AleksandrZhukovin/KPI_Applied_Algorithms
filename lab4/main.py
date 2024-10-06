from lab1.list import List, Node


class SetNode(Node):
    """
    Modify lab1 Node class to add link on header(set)
    """
    def __init__(self, *args, header):
        super().__init__(*args)
        self.header = header

    def __lt__(self, other):
        return self.index < other.index


class SetList(List):
    """
    Modify lab1 List class to add root(name) of Set
    """
    def __init__(self, *, root):
        super().__init__()
        self.root = root

    def add(self, node):
        node.header = self
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1


class UnionFind:
    def __init__(self):
        self.sets = []
        self.roots = [0]

    def make_set(self, node):
        new_root = self.roots[-1] + 1
        new_list = SetList(root=new_root)
        new_list.add(node)
        self.sets.append(new_list)

    @staticmethod
    def find(node):
        return node.header

    def union(self, node1, node2):
        set1 = self.find(node1)
        set2 = self.find(node2)

        if set1 == set2:
            return

        if len(set1) < len(set2):
            set1, set2 = set2, set1

        current = set2.head
        while current:
            current.header = set1
            current = current.next

        if set1.tail:
            set1.tail.next = set2.head
        else:
            set1.head = set2.head
        set1.tail = set2.tail
        set1.length += set2.length

        self.sets.remove(set2)
