"""
Сортировки обменами (метод пузырька, чётно-нечётная сортировка)

Сортировки выбором (сортировка выбором, бинго-сортировка)

Сортировки вставками (сортировка простыми вставками, метод Шелла)
"""
from dataclasses import dataclass
from time import time
from random import randint
import requests


@dataclass
class Algorithm:
    name: str
    type: str
    complexity: str
    code_lines_count: int
    code: str


@dataclass
class Data:
    sort_percentage: int
    item_count: int
    items: list[int]

    def copy(self):
        """Возвращает полную копию списка элементов."""
        return self.items.copy()


@dataclass
class Sorted:
    algorithm: Algorithm
    raw_data: Data
    sorted_data: list[int]
    time: float
    iter_count: int
    replacements_count: int


#! Сортировки обменами


def bubble(raw_data: Data):
    """Сортировка пузырьком. Возвращает отсортированный массив"""
    code = (
        """
def bubble(raw_data: list[int]):
    data = raw_data.copy()

    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]

    return data
""")
    algorithm = Algorithm('Пузырьковая', 'Обменами', 'O(n²)', 3, code)
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    for i in range(len(data) - 1):
        if data[i] > data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            replacements_count += 1

        iter_count += 1

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


def odd_even(raw_data: Data):
    """Чётно-нечётная сортировка. Возвращает отсортированный массив"""
    code = (
        """
def odd_even(raw_data: list[int]):
    data = raw_data.copy()

    n = len(data)
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0

        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                isSorted = 0

        for i in range(0, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                isSorted = 0

    return data
""")
    algorithm = Algorithm('Чёт-нечет', 'Обменами', 'O(n²)', 13, code)
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    n = len(data)
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        temp = 0

        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                replacements_count += 1
                isSorted = 0
            iter_count += 1

        for i in range(0, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                replacements_count += 1
                isSorted = 0
            iter_count += 1

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


#! Сортировки выбором


def selection(raw_data: Data):
    """Сортировка выбором. Возвращает отсортированный массив"""
    code = (
        """
def selection(raw_data: list[int]):
    data = raw_data.copy()

    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e

    return data
""")
    algorithm = Algorithm('Выбором', 'Выбором', 'O(n²)', 3, code)
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
        replacements_count += 1
        iter_count += len(range(i, len(data)))

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


def bingo(raw_data: Data):
    """Бинго-сортировка. Возвращает отсортированный массив"""
    code = (
        """
def bingo(raw_data: list[int]):
    data = raw_data.copy()

    # Первый проход.
    max = len(data) - 1
    nextValue = data[max]
    for i in range(max - 1, -1, -1):
        if data[i] > nextValue:
            nextValue = data[i]

    while max and data[max] == nextValue:
        max -= 1

    # Последующие проходы.
    while max:
        value = nextValue
        nextValue = data[max]

        for i in range(max - 1, -1, -1):
            if data[i] == value:
                data[i], data[max] = data[max], data[i]
                max -= 1
            elif data[i] > nextValue:
                nextValue = data[i]

        while max and data[max] == nextValue:
            max -= 1

    return data
""")
    algorithm = Algorithm('Бинго', 'Выбором', 'O(n²)', 18, code)
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    # Первый проход.
    max = len(data) - 1
    nextValue = data[max]
    for i in range(max - 1, -1, -1):
        if data[i] > nextValue:
            nextValue = data[i]
        iter_count += 1

    while max and data[max] == nextValue:
        max -= 1
        iter_count += 1

    # Последующие проходы.
    while max:
        value = nextValue
        nextValue = data[max]

        for i in range(max - 1, -1, -1):
            if data[i] == value:
                data[i], data[max] = data[max], data[i]
                replacements_count += 1
                max -= 1
            elif data[i] > nextValue:
                nextValue = data[i]
            iter_count += 1

        while max and data[max] == nextValue:
            max -= 1
            iter_count += 1

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


#! Сортировки вставками


def insertion(raw_data: Data):
    """Сортировка простыми вставками. Возвращает отсортированный массив"""
    code = (
        """
def insertion(raw_data: list[int]):
    data = raw_data.copy()

    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

    return data
""")
    algorithm = Algorithm('Простыми вставками', 'Вставками', 'O(n²)', 18, code)
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while data[j] > key and j >= 0:
            data[j + 1] = data[j]
            replacements_count += 1
            j -= 1
        data[j + 1] = key
        iter_count += 1

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


def shell(raw_data: Data):
    """Сортировка методом Шелла. Возвращает отсортированный массив"""
    code = (
        """
def shell(raw_data: list[int]):
    data = raw_data.copy()

    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

    return data
""")

    algorithm = Algorithm('Метод Шелла', 'Вставками', 'O(n×log²n))', 18, code)
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                replacements_count += 1
                i -= inc
            data[i] = el
            iter_count += 1
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


#! Вспомогательные функции для тестирования


def generate_data(sort_percentage: int, item_count: int):
    data: list[int] = []
    sorted_part = int(sort_percentage / 100 * item_count)
    data = (
        [i for i in range(sorted_part)]
        + [
            randint(sorted_part, item_count)
            for i in range(sorted_part, item_count)
        ]
    )
    return Data(sort_percentage, item_count, data)


def add_algo_results(result: Sorted):
    api_url = "http://localhost:8000/api/algorithms/"
    response = requests.post(
        api_url,
        json={
            "name": result.algorithm.name,
            "type": result.algorithm.type,
            "complexity": result.algorithm.complexity,
            "sort_percentage": result.raw_data.sort_percentage,
            "item_count": result.raw_data.item_count,
            "time": result.time,
            "iter_count": result.iter_count,
            "replacements_count": result.replacements_count,
            "code_lines_count": result.algorithm.code_lines_count,
            "code": result.algorithm.code
        },
        auth=('api_worker', '1qa2ws3edZxc!')
    )
    print(response.text)


percents = [0, 10, 25, 33, 50, 75, 90]
item_counts = [500, 1000, 2500, 5000]
datasets: list[Data] = []
algos = [bubble, odd_even, selection, bingo, insertion, shell]

for percent in percents:
    for item_count in item_counts:
        datasets.append(generate_data(percent, item_count))

for dataset in datasets:
    for algo in algos:
        add_algo_results(algo(dataset))


# add_algo_results(bingo(generate_data(33, 2500)))
