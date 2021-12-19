import logger


class FlatIterator:
    def __init__(self, list):
        self.list = list
        self.index = 0
        self.subindex = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.subindex = self.subindex + 1
        if len(self.list[self.index]) == self.subindex:
            self.subindex = -1
            self.index = self.index + 1
            if len(self.list) == self.index:
                raise StopIteration
            return self.__next__()
        return self.list[self.index][self.subindex]


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def homework():
    return [item for item in FlatIterator(nested_list)]


logger.logger("log.txt", homework)()
