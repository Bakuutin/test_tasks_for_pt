# Original Tasks

## Task 1

Analyze the examples. Implement `my_code()`

#### First example

    >>> my_code({
            'first': 'first_value',
            'second': 'second_value'
        })
    
    first:
     first_value
    second:
     second_value
    
#### Second Example

    >>> my_code({
            '1': {
                'child': '1/child/value'
            },
            '2': '2/value'
        })
    
    1:
     child:
     1/child/value
    2:
     2/value

## Task 2.1

Implement the function `my_code()`. It must print the achievable nodes of the graph.

#### First example

    >>> data = {
            1: [2, 3],
            2: [4]
        }

    >>> my_code(data, 1)

    1
    2
    4
    3

#### Second Example

    >>> data = {
            1: [2, 3],
            2: [3, 4],
            4: [1]
        }

    >>> my_code(data, 1)

    1
    2
    3
    4
    
## Task 2.2

Same as previous, but now the recursive function cannot change its arguments.
