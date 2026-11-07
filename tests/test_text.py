from textkit.text import is_palindrome, word_count


def test_word_count():
    assert word_count("hello big world") == 3
    assert word_count("") == 0


def test_is_palindrome_simple():
    assert is_palindrome("racecar") is True
    assert is_palindrome("a") is True


def test_is_palindrome_ignores_case():
    assert is_palindrome("RaceCar") is True


def test_is_palindrome_ignores_non_alphanumerics():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("No 'x' in Nixon") is True


def test_is_palindrome_digits():
    assert is_palindrome("12321") is True
    assert is_palindrome("123") is False
    assert is_palindrome("1a2") is False


def test_is_palindrome_non_palindromes():
    assert is_palindrome("hello") is False
    assert is_palindrome("ab") is False


def test_is_palindrome_empty_or_symbols_only():
    assert is_palindrome("") is True
    assert is_palindrome("!!  ,") is True
