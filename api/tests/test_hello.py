"""Hello unit test module."""

from subscription.hello import hello


def test_hello():
    """Test the hello function."""
    assert hello() == "Hello subscription"
