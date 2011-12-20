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
class MultiReturn(object):
    """
    Takes a list and returns it one item at a time.

    :param returns:
        A list containing the things to be returned by
        :meth:`.MultiReturn.side_effect`, in order.
    """

    def __init__(self, returns):
        self.returns = returns

    def side_effect(self, *args, **kwargs):
        return self.returns.pop(0)
