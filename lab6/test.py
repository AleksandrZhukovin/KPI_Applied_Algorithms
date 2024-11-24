import random
import time

from main import *


data_sizes = [1000, 10000, 100000]
data_types = {
    'sorted': lambda size: list(range(size)),
    'random': lambda size: random.sample(range(size), size),
    'almost_sorted': lambda size: (lambda l: l[:size//2] + sorted(l[size//2:], key=lambda x: -x))(list(range(size))),
    'reverse_sorted': lambda size: list(range(size, 0, -1)),
    'few_unique': lambda size: [i % 10 for i in range(size)]
}

for elements_num in data_sizes:
    print("="*10)
    print(f'Тест масива розміром {elements_num}')
    print("=" * 10)
    for data_type, generator in data_types.items():
        print("-" * 5)
        print(data_type)
        print("-" * 5)

        d = generator(elements_num)

        print('Рекурсія')
        start_time = time.time()
        top_down_merge_sort(d.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        print("Час: ", execution_time, '\n')

        print('Ітерований')
        start_time = time.time()
        bottom_up_merge_sort(d.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        print("Час: ", execution_time, '\n')

        print('Оптимізований')
        start_time = time.time()
        bottom_up_merge_sort_optimized(d.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        print("Час: ", execution_time, '\n')

        print('На 10')
        start_time = time.time()
        bottom_up_merge_sort_10(d.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        print("Час: ", execution_time, '\n')
