from foo import say_foo


def test_something_ok():
    print("run test_something_else")
    assert say_foo("World") == "Foo World!"
