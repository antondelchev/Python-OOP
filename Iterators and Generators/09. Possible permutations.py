import itertools


def possible_permutations(list_of_nums):
    current = 0
    all_done = list(itertools.permutations(list_of_nums))
    while current < len(all_done):
        yield list(all_done[current])
        current += 1


[print(n) for n in possible_permutations([1, 2, 3])]
