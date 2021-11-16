class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.start = 0
        self.end = len(self.dict_obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        keys = [key for key in self.dict_obj.keys()]
        k = keys[self.start]
        v = self.dict_obj[k]
        self.start += 1
        return k, v


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
