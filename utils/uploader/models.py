from dataclasses import dataclass


@dataclass
class Algorithm:
    name: str
    type: str
    complexity: str
    code_lines_count: int
    code: str
    description: str


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
