from collections import Counter
from nose.tools import assert_true, assert_false


def check_permutation(string: str, string2: str) -> bool:
    return Counter(string) == Counter(string2)


def check_permutation2(string: str, string2: str) -> bool:
    if len(string) != len(string2):
        return False

    dstr1 = {}
    for c in string:
        if c not in dstr1:
            dstr1[c] = 0
        dstr1[c] += 1

    for c in string2:
        if c not in dstr1:
            return False
        if dstr1[c] == 0:
            return False
        dstr1[c] -= 1
    return True


class TestCheckPermutation:

    def test_check_permutation(self):
        assert_true(check_permutation('abab', 'baba'))
        assert_true(check_permutation('abca', 'caba'))
        assert_false(check_permutation('abc', 'bc'))
        assert_false(check_permutation('abcd', 'abcc'))
        assert_false(check_permutation('abcc', 'abcd'))
        assert_true(check_permutation('', ''))

    def test_check_permutation2(self):
        assert_true(check_permutation2('abab', 'baba'))
        assert_true(check_permutation2('abca', 'caba'))
        assert_false(check_permutation2('abc', 'bc'))
        assert_false(check_permutation2('abcd', 'abcc'))
        assert_false(check_permutation2('abcc', 'abcd'))
        assert_true(check_permutation2('', ''))
