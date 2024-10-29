"""For testing the envgpt module."""

from src.envgpt.envgpt import hello_world


def test_test():
    """Test test"""
    assert 1 == 1


def test_hello_world():
    """Test hello_world"""
    assert hello_world("Hello world", False) == "Hello world"
