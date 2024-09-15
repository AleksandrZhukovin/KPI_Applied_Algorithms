import time
import random
import matplotlib.pyplot as plt

from set import Set

search_times_existing = []
search_times_non_existing = []
intersection_times = []

set_sizes = [10, 100, 1000, 10000,]

set1 = Set()
set2 = Set()

for size in set_sizes:
    intersection_sample_times = []
    search_existing_times = []
    search_non_existing_times = []

    for _ in range(1000):
        set1.clear()
        set2.clear()

        elements1 = random.sample(range(size * 2), size)
        elements2 = random.sample(range(size * 2), size)

        for e in elements1:
            set1.add(e)
        for e in elements2:
            set2.add(e)

        start = time.time()
        set1.search(elements1[random.randint(0, size - 1)])
        end = time.time()
        search_existing_times.append(end - start)

        start = time.time()
        set1.search(size + random.randint(1, size))
        end = time.time()
        search_non_existing_times.append(end - start)

        start = time.time()
        set1.intersection(set2)
        end = time.time()
        intersection_sample_times.append(end - start)

    avg_search_existing_time = sum(search_existing_times) / 1000
    avg_search_non_existing_time = sum(search_non_existing_times) / 1000
    avg_intersection_time = sum(intersection_sample_times) / 1000

    search_times_existing.append(avg_search_existing_time)
    search_times_non_existing.append(avg_search_non_existing_time)
    intersection_times.append(avg_intersection_time)

plt.figure(figsize=(12, 8))

plt.plot(set_sizes, search_times_existing, label='Пошук існуючого елементу', marker='o')
plt.plot(set_sizes, search_times_non_existing, label='Пошук неіснуючого елементу', marker='o')
plt.plot(set_sizes, intersection_times, label='Перетин', marker='o')

plt.xlabel('Потужність множинин')
plt.ylabel('Час виконання')
plt.legend()
plt.xscale('log')
plt.grid(True)
plt.show()
