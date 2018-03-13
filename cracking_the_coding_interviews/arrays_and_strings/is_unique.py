from nose.tools import assert_equal


def is_unique(string: str) -> bool:
    if len(string) > 26:
        return False

    hash_ = [False] * 26
    _a = ord('a')
    for c in string:
        if hash_[ord(c) - _a]:
            return False
        else:
            hash_[ord(c) - _a] = True
    return True


def is_unique_2(string: str) -> bool:
    if len(string) > 26:
        return False

    flag = 0
    for c in string:
        bit = 1 << ord(c) - ord('a')
        if flag & bit:
            return False
        flag |= bit
    return True


class TestIsUnique:

    def test_unique_strings(self):
        strs = ['apple', 'banana', 'fox', 'news', 'lessons']
        unique = [is_unique(s) for s in strs]
        assert_equal(unique, [False, False, True, True, False])

    def test_unique_strings_2(self):
        strs = ['apple', 'banana', 'fox', 'news', 'lessons']
        unique = [is_unique_2(s) for s in strs]
        assert_equal(unique, [False, False, True, True, False])
