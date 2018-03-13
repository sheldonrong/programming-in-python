from nose.tools import assert_equal, assert_true, assert_false


def palindrome_permutation(string: str) -> bool:
    """what we are checking is essentially that at most
    one character has frequency % 2 == 1"""
    freq = {}
    for c in string.lower():
        if c == ' ':
            continue
        if c not in freq:
            freq[c] = 0
        freq[c] += 1
    no_of_odd_chars = 0
    for v in freq.values():
        if v % 2 == 1:
            if no_of_odd_chars == 1:
                return False
            no_of_odd_chars += 1
    return True


class TestPalindromePermutation:

    def test_basic_strings(self):
        assert_true(palindrome_permutation('abcba'))
        assert_true(palindrome_permutation('abccba'))
        assert_true(palindrome_permutation('bc  baa'))
        assert_true(palindrome_permutation('cc b a a b'))

    def test_palindrome_permutation(self):
        test_cases = [
            ('Tact Coa', True),
            ('jhsabckuj ahjsbckj', True),
            ('Able was I ere I saw Elba', True),
            ('So patient a nurse to nurse a patient so', False),
            ('Random Words', False),
            ('Not a Palindrome', False),
            ('no x in nixon', True),
            ('azAZ', True)
        ]
        for test_case, is_palindrome_permutation in test_cases:
            assert_equal(
                palindrome_permutation(test_case),
                is_palindrome_permutation
            )
