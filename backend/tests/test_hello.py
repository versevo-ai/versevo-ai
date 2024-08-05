"""Hello unit test module."""

from platform.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello platform"
