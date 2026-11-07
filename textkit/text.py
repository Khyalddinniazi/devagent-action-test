"""Small text helpers."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Return True if ``text`` reads the same both ways, ignoring case and non-alphanumerics."""
    cleaned = [ch.casefold() for ch in text if ch.isalnum()]
    return cleaned == cleaned[::-1]
