from array_and_lists.linked_list import ListElement
from nose.tools import assert_true, assert_false, assert_equal


class TestListElement:

    def setup(self):
        self.e1 = ListElement(1)
        self.e2 = ListElement(2)
        self.e3 = ListElement(3)

        self.e1.next_ = self.e2
        self.e2.next_ = self.e3

    def test__contains__(self):
        assert_true(3 in self.e1)
        assert_true(3 in self.e2)
        assert_true(3 in self.e3)
        assert_false(4 in self.e1)
        assert_false(4 in self.e2)
        assert_false(4 in self.e3)

    def test_find(self):
        e3 = self.e1.find(3)
        assert_equal(e3.data, 3)
        assert_equal(e3.next_, None)

        e4 = self.e1.find(4)
        assert_equal(e4, None)
