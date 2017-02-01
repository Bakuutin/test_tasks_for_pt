def my_code(data, offset=0, offset_string='  '):
    for key, value in sorted(data.items()):
        print(offset_string * offset, key, ':', sep='')

        if isinstance(value, dict):
            my_code(value, offset + 1, offset_string)
        else:
            print(offset_string * (offset + 1), value, sep='')


if __name__ == '__main__':
    my_code({
        'first': 'first_value',
        'second': 'second_value',
    })

    print()

    my_code({
        '1': {
            'child': '1/child/value'
        },
        '2': '2/value'
    })
