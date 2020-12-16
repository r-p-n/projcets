class SparseArray:

    class Node:
        def __init__(self, data, next_node, previous_node, array_index):
            self.array_index = array_index
            self.data = data
            self.next_node = next_node
            self.previous_node = previous_node

        def get_data(self):
            return self.data

        def set_data(self, data):
            self.data = data

        def get_next_node(self):
            return self.next_node

        def set_next_node(self, node):
            self.next_node = node

        def get_array_index(self):
            return self.array_index

        def get_previous_node(self):
            return self.previous_node

        def set_previous_node(self, node):
            self.previous_node = node

    def __init__(self, size):
        self.array = [None] * size
        self.root = None
        self.tail = None
        self.size = size
        self.usage = 0

    def __len__(self):
        return self.size

    def __getitem__(self, j):
        if self.array[j] is not None:
            return self.array[j].get_data()

    def __setitem__(self, j, e):
        if self.array[j] is not None:
            self.array[j].set_data(e)
            return
        if e is None:
            self.delete_element(j)
            return
        if not self.usage == 0:
            self.root.set_next_node(self.Node(e, None, self.root, j))
            self.root = self.root.get_next_node()
            self.array[j] = self.root
        else:
            self.array[j] = self.Node(e, None, None, j)
            self.root = self.array[j]
            self.tail = self.array[j]
        self.usage += 1

    def delete_element(self, j):
        if self.usage == 1:
            self.array[j] = None
            self.root = None
            self.tail = None
            self.usage = 0
            return
        current = self.root
        for i in range(0, self.usage):
            if current.get_array_index() == j:
                if not current == self.root and not current == self.tail:
                    current.get_next_node().set_previous_node(current.get_previous_node())
                    current.get_previous_node().set_next_node(current.get_next_node())
                elif current == self.root:
                    self.root = current.get_previous_node()
                    self.root.set_next_node(None)
                elif current == self.tail:
                    self.tail = current.get_next_node()
                    self.tail.set_previous_node(None)
                self.array[j] = None
                self.usage -= 1
                break
            current = current.get_previous_node()

    def fill(self, seq):
        if len(seq) > self.size - self.usage:
            raise ValueError("Sequence size is too large.")
        n = 0
        for i in seq:
            while self.array[n] is not None:
                n += 1
            self.__setitem__(n, i)

    def get_usage(self):
        return self.usage
