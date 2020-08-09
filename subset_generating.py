def process_larger_subsets(my_set, subset, subset_size, next_index):
    if subset_size == len(subset):
        print(list(subset))
    else:
        for i in range(next_index, len(my_set)):
            subset[subset_size] = my_set[i]
            process_larger_subsets(my_set, subset, subset_size + 1, i + 1)


def process_subsets(my_set, k):
    subset = list(range(k))
    process_larger_subsets(my_set, subset, 0, 0)


set_1 = [1, 2, 3, 4, 5, 6]
process_subsets(set_1, 4)
