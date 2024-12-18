import random

from main import *


def generate_test_data(size):
    data_sets = {
        "identical": [1] * size,
        "sorted": list(range(size)),
        "random": [random.randint(0, size) for _ in range(size)],
        "almost_sorted": sorted(list(range(size))),
        "reverse_sorted": list(range(size, 0, -1)),
        "triangular": list(range(size // 2)) + list(range(size // 2, 0, -1)),
        "few_unique": [random.randint(0, 5) for _ in range(size)]
    }

    for i in range(int(size * 0.05)):
        idx1, idx2 = random.sample(range(size), 2)
        data_sets["almost_sorted"][idx1], data_sets["almost_sorted"][idx2] = data_sets["almost_sorted"][idx2], \
            data_sets["almost_sorted"][idx1]

    return data_sets


sizes = [500, 1000, 1500]
algorithms = [
    sort_lomuto_last,
    sort_lomuto_random,
    sort_lomuto_median_three,
    sort_lomuto_median_random,
    sort_hoare_last,
    sort_hoare_random,
    sort_hoare_median_three,
    sort_hoare_median_random,
    sort_three_quicksort,
    sort_with_dual_pivot,
]

for size in sizes:
    data_sets = generate_test_data(size)
    for data_type, data in data_sets.items():
        print(f"\nДовжина масиву: {size}\n")
        for algorithm in algorithms:
            test_data = data[:]
            print(f"{algorithm.__name__}|{data_type}")
            algorithm(test_data)
            print()
