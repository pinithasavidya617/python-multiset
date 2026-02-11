class Multiset:

    def __init__(self):
        self.data = {}

    def add(self, val):
        if val in self.data:
            self.data[val] += 1
        else:
            self.data[val] = 1

    def remove(self, val):
        if val in self.data:
            self.data[val] -= 1
            if self.data[val] == 0:
                del self.data[val]

    def __contains__(self, val):
        return val in self.data

    def __len__(self):
        return sum(self.data.values())

    def __str__(self):
        return str(self.data)

m = Multiset()
m.add(5)
print(m.__contains__(3))
print(m)