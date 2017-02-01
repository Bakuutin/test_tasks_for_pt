from task2_immutable import my_code


def test_first_case(capsys):
    my_code({1: [2, 3], 2: [3, 4], 4: [1]}, 1)
    out, err = capsys.readouterr()
    assert out.split() == ['1', '2', '3', '4']


def test_second_case(capsys):
    my_code({1: [2, 3], 2: [4]}, 1)
    out, err = capsys.readouterr()
    assert out.split() == ['1', '2', '4', '3']
