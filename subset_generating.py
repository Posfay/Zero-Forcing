"""
Generate subsets from a set recursively.
"""


subsets = list()


def process_larger_subsets(my_set, subset, subset_size, next_index):
"""
NIT: Please add Docstring.
"""
    if subset_size == len(subset):
        subsets.append(list(subset))
    else:
        for i in range(next_index, len(my_set)):
            subset[subset_size] = my_set[i]
            process_larger_subsets(my_set, subset, subset_size + 1, i + 1)


def process_subsets(my_set, k):
    """
    Generate all subsets of length k from my_set
    
    :param my_set: list
    :param k: int
    :return: list
    """
    subsets.clear()
    subset = list(range(k))
    process_larger_subsets(my_set, subset, 0, 0)
    return list(subsets)
