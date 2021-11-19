def get_primes(list_of_nums):
    for el in list_of_nums:
        if el == 0 or el == 1:
            continue
        counter = 0
        for num in range(1, el + 1):
            if el % num == 0:
                counter += 1
        if counter <= 2:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
