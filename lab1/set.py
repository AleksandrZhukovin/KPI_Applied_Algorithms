from list import List


class Set(List):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Set | {self.length} els"

    def search(self, cargo, n=None):
        if n is None:
            n = self.head
        while n is not None:
            if cargo == n.cargo:
                return n
            n = n.next
        return None

    def add(self, cargo):
        exists = True if self.search(cargo) else False
        if not exists:
            super().add(cargo)

    def remove(self, cargo):
        super().remove(cargo)

    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    def union(self, set_):
        result = Set()

        current = self.head
        while current is not None:
            result.add(current.cargo)
            current = current.next

        current = set_.head
        while current is not None:
            result.add(current.cargo)
            current = current.next
        return result

    def intersection(self, set_):
        result = Set()

        current = self.head
        while current is not None:
            if set_.search(current.cargo):
                result.add(current.cargo)
            current = current.next
        return result

    def difference(self, set_):
        result = Set()

        current = self.head
        while current is not None:
            if not set_.search(current.cargo):
                result.add(current.cargo)
            current = current.next
        return result

    def symmetric_difference(self, set_):
        result = Set()

        current = self.head
        while current is not None:
            if not set_.search(current.cargo):
                result.add(current.cargo)
            current = current.next

        current = set_.head
        while current is not None:
            if not self.search(current.cargo):
                result.add(current.cargo)
            current = current.next
        return result

    def is_subset(self, set_):
        current = self.head
        while current is not None:
            if not set_.search(current.cargo):
                return False
            current = current.next
        return True
