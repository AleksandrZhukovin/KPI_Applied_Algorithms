class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class List:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def __str__(self):
        return f"List | {self.length} els"

    def __len__(self):
        return self.length

    def add(self, cargo):
        new_node = Node(cargo)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, cargo):
        if self.length == 0:
            raise ValueError("List is empty")

        current = self.head
        previous = None

        while current is not None:
            if current.cargo == cargo:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                if current == self.tail:
                    self.tail = previous

                self.length -= 1
                break
            previous = current
            current = current.next
