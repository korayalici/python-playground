from python_playground.main import greet, is_even, slugify


def test_greet():
    assert greet("Koray") == "Hello, Koray!"

def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False

def test_slugify():
    assert slugify("Hello World") == "hello-world"
    assert slugify("Python Playground") == "python-playground"

def test_slugify_collapses_spaces():
    assert slugify("Hello    World") == "hello-world"

def test_slugify_strips_punctuation():
    assert slugify("Hello, World!!!") == "hello-world"

def test_slugify_trims():
    assert slugify("  Hello World  ") == "hello-world"
