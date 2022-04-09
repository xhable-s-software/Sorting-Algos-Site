"""
Сортировки обменами (метод пузырька, чётно-нечётная сортировка)

Сортировки выбором (сортировка выбором, бинго-сортировка)

Сортировки вставками (сортировка простыми вставками, метод Шелла)
"""
from time import time
from random import randint
import requests
from models import Algorithm, Data, Sorted
from algos import algos
from loguru import logger


#! Сортировки обменами


def bubble(raw_data: Data):
    """Сортировка пузырьком. Возвращает отсортированный массив"""
    algorithm = algos.bubble
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
    algorithm = algos.odd_even
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
    algorithm = algos.selection
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
    algorithm = algos.bingo
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


def heapify(nums, heap_size, root_index, replacements_count: int = 0):
    # Индекс наибольшего элемента считаем корневым индексом

    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — допустимый индекс, а элемент больше,
    # чем текущий наибольший, обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
        replacements_count += 1

    # То же самое для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
        replacements_count += 1

    # Если наибольший элемент больше не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        replacements_count += 1
        # Heapify the new root element to ensure it's the largest
        return heapify(nums, heap_size, largest, replacements_count)

    return replacements_count


def heap_sort(raw_data: Data):
    """Пирамидальная сортировка. Возвращает отсортированный массив"""
    algorithm = algos.heap
    data = raw_data.copy()
    start_time = time()
    iter_count = 0
    replacements_count = 0

    n = len(data)

    # Создаём Max Heap из списка
    # Второй аргумент означает остановку алгоритма перед элементом -1, т.е.
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении,
    # уменьшая счётчик i на 1
    for i in range(n, -1, -1):
        iter_count += 1
        heapify(data, n, i)

    # Перемещаем корень Max Heap в конец списка
    for i in range(n - 1, 0, -1):
        iter_count += 1
        data[i], data[0] = data[0], data[i]
        replacements_count += 1
        replacements_count += heapify(data, i, 0)

    work_time = round((time() - start_time) * 1000, 3)
    return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


def merge(raw_left: Data, raw_right: Data):
    algorithm: Algorithm = algos.merge
    # Sorted(algorithm, raw_data, data, work_time,
    #        iter_count, replacements_count)
    iter_count = 0
    replacements_count = 0
    left, right = raw_left.copy(), raw_right.copy()
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
            replacements_count += 1
        else:
            result.append(right[0])
            right = right[1:]
            replacements_count += 1
        iter_count += 1
    if len(left) > 0:
        result += left
        replacements_count += len(left)
    if len(right) > 0:
        result += right
        replacements_count += len(left)

    return result, iter_count, replacements_count


def merge_sort(raw_data: Data, data=None, replacements_count: int = 0, iter_count: int = 0, start_time: float = time()):
    """Сортировка слиянием. Возвращает отсортированный массив"""
    algorithm: Algorithm = algos.merge
    if data is None:
        data = raw_data.copy()

    # print(data)
    n = len(data)
    if n <= 1:
        work_time = round((time() - start_time) * 1000, 3)
        return Sorted(algorithm, raw_data, data, work_time,
                      iter_count, replacements_count)
    else:
        middle = int(len(data) / 2)
        left = merge_sort(raw_data, data[:middle],
                          replacements_count, iter_count, start_time)
        right = merge_sort(raw_data, data[middle:],
                           replacements_count, iter_count, start_time)

        work_time = round((time() - start_time) * 1000, 3)

        data, iter_inc, replacements_inc = merge(
            left.sorted_data, right.sorted_data)

        iter_count += iter_inc
        replacements_count += replacements_inc
        return Sorted(algorithm, raw_data, data, work_time, iter_count, replacements_count)


#! Сортировки вставками


def insertion(raw_data: Data):
    """Сортировка простыми вставками. Возвращает отсортированный массив"""
    algorithm = algos.insertion
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
    algorithm = algos.shell
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
            "code": result.algorithm.code,
            "description": result.algorithm.description
        },
        auth=('api_worker', '1qa2ws3edZxc!')
    )


def mass_upload():
    percents = [0, 10, 25, 33, 50, 75, 90]
    item_counts = [500, 1000, 2500, 5000]
    datasets: list[Data] = []
    # fn_algos = [bubble, odd_even, selection, bingo, insertion, shell]
    fn_algos = [merge_sort]

    for percent in percents:
        for item_count in item_counts:
            datasets.append(generate_data(percent, item_count))

    for dataset in datasets:
        for algo in fn_algos:
            logger.debug(
                f"Добавление {algo.__name__}  ({dataset.item_count}/{dataset.sort_percentage}%)... ")
            add_algo_results(algo(dataset))
            logger.success(
                f"Добавлено: {algo.__name__} ({dataset.item_count}/{dataset.sort_percentage}%).")


mass_upload()


# add_algo_results(bingo(generate_data(33, 2500)))
