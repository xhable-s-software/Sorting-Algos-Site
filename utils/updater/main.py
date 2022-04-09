from algos import algos
import requests
from loguru import logger

auth = ('api_worker', '1qa2ws3edZxc!')


def replace_description(algo_name: str, new_description: str):
    logger.debug(
        f'[>] Starting to replace the descriptions for name {algo_name}...')

    api_url = "http://localhost:8000/api/algorithms/"
    response = requests.get(
        api_url,
        auth=auth
    )

    json_response = response.json()
    correct_urls = []

    for obj in json_response:
        if obj['name'] == algo_name:
            correct_urls.append(obj['url'])

    for url in correct_urls:
        response = requests.patch(
            url,
            json={"description": new_description},
            auth=auth
        )
        logger.debug(f'Replaced obj\'s desc with pk {url.split("/")[-2]}.')

    logger.success(
        f'[v] Replaced desc in {len(correct_urls)} objects (name - {algo_name}).')


for algo in list(algos.values()):
    print(algo)
    replace_description(algo.name, algo.description)
# print()
# print(len(algos.values()))
# replace_description()
