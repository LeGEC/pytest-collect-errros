from foo import say_foo


def say_bar(name: str):
    sfoo = say_foo(name)
    return f"Bar {sfoo}"
