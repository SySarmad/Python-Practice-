from collections import Counter

"""Count words."""


def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    counted_words = Counter(s.split())
    frequent = []

   # TODO: Count the number of occurences of each word in s
    for word, freq in counted_words.items():
        if freq == n:
            frequent.append((word, n))

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    sorted_list = sorted(frequent, reverse=False)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = tuple(sorted_list)

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit bit bit of butter but but but the butter was bitter", 3)
    print

if __name__ == '__main__':
    test_run()