subsets = list()


def process_larger_subsets(my_set, subset, subset_size, next_index):

    if subset_size == len(subset):
        subsets.append(list(subset))
    else:
        for i in range(next_index, len(my_set)):
            subset[subset_size] = my_set[i]
            process_larger_subsets(my_set, subset, subset_size + 1, i + 1)


def process_subsets(my_set, k):

    subsets.clear()
    subset = list(range(k))
    process_larger_subsets(my_set, subset, 0, 0)
