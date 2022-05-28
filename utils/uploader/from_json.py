import json
from algos import algos
from models import Algorithm, Sorted, Data
from main import add_algo_results
from loguru import logger

"""Структура входного файла
[
    {
        "item_count": 500,
        "iter_count": 0,
        "name": "_sort",
        "replacements_count": 0,
        "sort_percentage": 0,
        "time": 0.18410000205039978
    },
    
    {
        "item_count": 500,
        "iter_count": 0,
        "name": "_stable_sort",
        "replacements_count": 0,
        "sort_percentage": 0,
        "time": 0.14309999346733093
    },

    ...
"""


def parse_json(path='./output.json'):
    with open(path, 'r') as file:
        j = json.load(file)

    for item in j:
        algo: Algorithm

        if item['name'] == '_sort':
            algo = algos.stl_sort
        elif item['name'] == '_stable_sort':
            algo = algos.stl_stable_sort
        elif item['name'] == '_heap_sort':
            algo = algos.stl_sort_heap

        result = Sorted(
            algorithm=algo,
            raw_data=Data(
                sort_percentage=item['sort_percentage'],
                item_count=item['item_count'],
                items=[]
            ),
            sorted_data=[],
            time=round(item['time'], 3),
            iter_count=item['iter_count'],
            replacements_count=item['replacements_count']
        )

        logger.debug(
            f"Добавление {algo.name}  ({result.raw_data.item_count}/{result.raw_data.sort_percentage}%)... ")
        response = add_algo_results(result)
        logger.success(
            f"Добавлено: {algo.name} ({result.raw_data.item_count}/{result.raw_data.sort_percentage}%).")
        # print(response.json())

        # print(algo)


parse_json()
