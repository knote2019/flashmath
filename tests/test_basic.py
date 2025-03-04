import cmake_example as m


def test_main():
    assert m.__version__ == "0.0.1"
    assert m.add(1, 2) == 3
    assert m.sub(1, 2) == -1
    print("pass !!!")
