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
