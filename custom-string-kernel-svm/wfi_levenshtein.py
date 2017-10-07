"""
~~~
Pure-python Levenshtein implementation made by https://github.com/toastdriven
~~~
"""


def wfi_levenshtein(str1, str2):
    """
    Calculates the Levenshtein distance between two strings.
    This version uses an iterative version of the Wagner-Fischer algorithm.
    The similarity tends to be closer as the value of the function approaches zero.
    :param str_1:
            string
                first input text used in a similarity calculation
    :param str_2:
            string
                second input text used in a similarity calculation
    :return:
            integer
                Returns a value of a Levenshtein similarity function

    >>> wfi_levenshtein('kitten', 'sitting')
        3
        >>> wfi_levenshtein('kitten', 'kitten')
        0
        >>> wfi_levenshtein('', '')
        0
    """
    
    if str_1 == str_2:
        return 0

    len_1 = len(str_1)
    len_2 = len(str_2)

    if len_1 == 0:
        return len_2
    if len_2 == 0:
        return len_1

    if len_1 > len_2:
        str_2, str_1 = str_1, str_2
        len_2, len_1 = len_1, len_2

    d0 = [i for i in range(len_2 + 1)]
    d1 = [j for j in range(len_2 + 1)]

    for i in range(len_1):
        d1[0] = i + 1
        for j in range(len_2):
            cost = d0[j]

            if str_1[i] != str_2[j]:
                # substitution
                cost += 1

                # insertion
                x_cost = d1[j] + 1
                if x_cost < cost:
                    cost = x_cost

                # deletion
                y_cost = d0[j + 1] + 1
                if y_cost < cost:
                    cost = y_cost

            d1[j + 1] = cost

        d0, d1 = d1, d0

    return d0[-1]
