def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word.

    :param word: str
    :return: int

    >>> count_vowels('Cusco')
    2

    >>> count_vowels('Manila')
    3

    >>> count_vowels('Istanbul')
    3
    """
    total_vowels = 0
    for letter in word.lower():
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels


def main():
    import doctest
    count_vowels("pengfei")
    doctest.testmod()


if __name__ == "__main__":
    main()
