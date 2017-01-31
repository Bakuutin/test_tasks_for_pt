def my_code(data, index, reached=None):
    if reached:
        if index in reached:
            return
        reached.add(index)
    else:
        reached = {index}

    print(index)

    for i in data.get(index, []):
        my_code(data, i, reached)


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
