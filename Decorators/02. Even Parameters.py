def even_parameters(func_ref):
    def wrapper(*args):
        for el in args:
            if isinstance(el, int) and el % 2 == 0:
                pass
            else:
                return "Please use only even numbers!"
        result = func_ref(*args)
        return result

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
