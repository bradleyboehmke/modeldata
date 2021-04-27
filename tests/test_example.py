"""Test example functionality."""
from modeldata import greeting


def test_greeting_default():
    """Default greeting output."""
    default = "Brad"
    assert greeting() == f"Hello {default}!"


def test_greeting_personalized():
    """Personalized greeting output."""
    assert greeting("Debbie") == "Hello Debbie!"
