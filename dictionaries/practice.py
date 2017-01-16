"""Dictionaries Practice

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """
    word_counter = {}
    ret = []

    for word in words:   # This method preserves order of first occurrences on the list.

        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
            ret.append(word)

        # word_tracker[word] = word_tracker.get(word, 0) + 1 # to count them

    return ret

    # return list(set(words)) doesn't use dictionaries :(
    # Other option I wrote first:
    #
    # for word in words:
    #     word_counter[word] = word_counter.get(word, 0) + 1
    #
    # return word_counter.keys()
    # I know I didn't NEED to preserve order but I liked it better that way.

def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    which_list = {}

    for item in items1:
        which_list[item] = 1

    for item in items2:
        if item in which_list and which_list[item] == 1:
            which_list[item] = 3
        elif item in which_list:
            pass
        else:
            which_list[item] = 2

    return [item for item in which_list if which_list[item] == 3]


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pairs summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    has_negatives = {}
    ret = []

    for num in numbers:
        if -num in has_negatives or num == 0:
            has_negatives[num] = True
            has_negatives[-num] = True
        else:
            has_negatives[num] = False

    for num in has_negatives:
        if has_negatives[num] == True:
            pair = sorted([num, -num])
            if pair not in ret:
                ret.append(pair)
    return ret
    # REFACTOR THIS!!!


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most in the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    character_counts = {}
    for char in phrase:
        if char != ' ':
            character_counts[char] = character_counts.get(char, 0) + 1

    most = 0
    winner = ['']
    for char, num in character_counts.items():
        if num > most:
            winner = [char]
            most = num
        elif num == most:
            winner.append(char)

    return sorted(winner, key=str.lower) # Lowercase to sort alphabetically.

#####################################################################
# You can ignore everything below this.


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


# Time spent Saturday: 50 mins

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
