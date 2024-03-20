from fooo import say_foo # <- wrong import, fails at import time


def test_something_import_failsw():
    print("run test_something_else")
    assert say_foo("World") == "Foo World!"
