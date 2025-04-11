"""Hello unit test module."""

from logging import root
from subscription.main import root


def test_hello():
    """Test the hello function."""
    assert root() == "Hello subscription"
