class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.extended_sq = self.sequence + self.sequence * (self.number - len(self.sequence))
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.number - 1:
            raise StopIteration
        if len(self.sequence) >= self.number:
            current_char = self.sequence[self.start]
        else:
            current_char = self.extended_sq[self.start]
        self.start += 1
        return current_char


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
