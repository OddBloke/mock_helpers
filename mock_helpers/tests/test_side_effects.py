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
