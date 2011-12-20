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
from nose.tools import assert_raises

from mock_helpers.assertions import assert_called_once


def test_not_called():
    """
    Test that :py:func:`.assert_called_once` fails if mock uncalled.
    """
    m = Mock()
    assert_raises(AssertionError, assert_called_once, m)


def test_called_twice():
    """
    Test that :py:func:`.assert_called_once` fails if mock called twice.
    """
    m = Mock()
    m()
    m()
    assert_raises(AssertionError, assert_called_once, m)


def test_called_with_only_args():
    """
    Test that :py:func:`.assert_called_once` works with only args.
    """
    m = Mock()
    m('test')
    assert_called_once(m, ('test',))
    assert_called_once(m, ('test',), {})
    assert_called_once(m, expected_args=('test',))
    assert_called_once(m, expected_kwargs={}, expected_args=('test',))


def test_called_with_incorrect_args():
    """
    Test that :py:func:`.assert_called_once` fails with wrong args.
    """
    m = Mock()
    m('not test')
    assert_raises(AssertionError, assert_called_once, m, ('test',))
    assert_raises(AssertionError, assert_called_once, m, ('test',), {})
    assert_raises(AssertionError,
                  assert_called_once, m, expected_args=('test',))
    assert_raises(AssertionError,
                  assert_called_once, m, expected_kwargs={},
                                      expected_args=('test',))


def test_called_with_only_kwargs():
    """
    Test that :py:func:`.assert_called_once` works with only kwargs.
    """
    m = Mock()
    m(test='test')
    assert_called_once(m, (), {'test': 'test'})
    assert_called_once(m, expected_kwargs={'test': 'test'})
    assert_called_once(m, expected_kwargs={'test': 'test'}, expected_args=())


def test_called_with_incorrect_kwargs():
    """
    Test that :py:func:`.assert_called_once` fails with wrong kwargs.
    """
    m = Mock()
    m(test='not test')
    assert_raises(AssertionError, assert_called_once, m, (), {'test': 'test'})
    assert_raises(AssertionError,
                  assert_called_once, m, expected_kwargs={'test': 'test'})
    assert_raises(AssertionError,
                  assert_called_once, m, expected_kwargs={'test': 'test'},
                                      expected_args=())


def test_called_with_args_and_kwargs():
    """
    Test that :py:func:`.assert_called_once` works with args and kwargs.
    """
    m = Mock()
    m('test', test='test')
    assert_called_once(m, ('test',), {'test': 'test'})
    assert_called_once(m,
                       expected_kwargs={'test': 'test'},
                       expected_args=('test',))


def test_called_with_correct_args_and_incorrect_kwargs():
    """
    Test that :py:func:`.assert_called_once` fails with args and wrong kwargs.
    """
    m = Mock()
    m('test', test='not test')
    assert_raises(AssertionError,
                  assert_called_once, m, ('test',), {'test': 'test'})
    assert_raises(AssertionError,
                  assert_called_once,
                       m,
                       expected_kwargs={'test': 'test'},
                       expected_args=('test',))


def test_called_with_incorrect_args_and_correct_kwargs():
    """
    Test that :py:func:`.assert_called_once` fails with kwargs and wrong args.
    """
    m = Mock()
    m('not test', test='test')
    assert_raises(AssertionError,
                  assert_called_once, m, ('test',), {'test': 'test'})
    assert_raises(AssertionError,
                  assert_called_once,
                       m,
                       expected_kwargs={'test': 'test'},
                       expected_args=('test',))


def test_called_with_mocklike_object():
    """
    Test that :py:func:`.assert_called_once` fails when called with non-Mock.
    """
    class NotMock(object):
        pass
    n = NotMock()
    n.call_count = 1
    n.call_args = ('', '')
    assert_raises(AssertionError, assert_called_once, n, '', '')

