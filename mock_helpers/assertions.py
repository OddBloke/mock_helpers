from mock import Mock


def assert_called_once(mock_obj, expected_args=None, expected_kwargs=None):
    """Assert ``mock`` called once with expected args/kwargs.

    :param mock.Mock mock: The Mock to assert against.
    :param expected_args:
        A tuple containing the expected positional arguments.
    :param expected_kwargs:
        A dictionary containing the expected keyword arguments.
    """
    assert isinstance(mock_obj, Mock)
    if expected_args is None:
        expected_args = ()
    if expected_kwargs is None:
        expected_kwargs = {}
    assert 1 == mock_obj.call_count, (
            "Mock called {0} times, not once.".format(mock_obj.call_count))
    args, kwargs = mock_obj.call_args
    assert expected_args == args
    assert expected_kwargs == kwargs
