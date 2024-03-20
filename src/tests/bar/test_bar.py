from bar import say_bar


def test_something():
    print("run test_something")
    assert say_bar("World") == "Bar Foo World!"
