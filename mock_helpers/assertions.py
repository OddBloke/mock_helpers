# This file is part of the mock_helpers library
# Copyright (C) 2011  Daniel Watkins
#
# The mock_helpers library is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
#
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
