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
from nose.tools import assert_equal, assert_raises

from mock_helpers.side_effects import MultiReturn


def test_multireturn_nothing():
    m = MultiReturn([])
    assert_raises(IndexError, m.side_effect)


def test_multireturn_one():
    m = MultiReturn([1])
    assert_equal(1, m.side_effect())
    assert_raises(IndexError, m.side_effect)


def test_multireturn_many():
    m = MultiReturn([1,2])
    assert_equal(1, m.side_effect())
    assert_equal(2, m.side_effect())
    assert_raises(IndexError, m.side_effect)


def test_multireturn_not_a_list():
    m = MultiReturn(2)
    assert_raises(AttributeError, m.side_effect)
