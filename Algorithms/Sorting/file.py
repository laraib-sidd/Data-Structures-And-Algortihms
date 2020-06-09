# global counter
counter = 0


def func(i):
    # global counter
    if i == 2:
        return 'done'
    i += 1
    print(i)
    return func(i)


print(func(counter))
