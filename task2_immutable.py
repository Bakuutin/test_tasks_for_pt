def my_real_code(data, index, reached=None):
    if reached:
        if index in reached:
            return reached
        reached |= {index}
    else:
        reached = frozenset({index})

    print(index)

    for i in data.get(index, []):
        reached = my_real_code(data, i, reached)

    return reached


def my_code(data, index):
    """
    Wrapper to not return any value
    """
    my_real_code(data, index)


if __name__ == '__main__':
    my_code({
        1: [2, 3],
        2: [4],
    }, 1)

    print()

    my_code({
        1: [2, 3],
        2: [3, 4],
        4: [1],
    }, 1)
