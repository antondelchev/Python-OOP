def type_check(expected_type):
    def decorator(func_ref):
        def wrapper(parameter):
            if expected_type == type(parameter):
                result = func_ref(parameter)
                return result
            else:
                return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
