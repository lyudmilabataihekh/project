from typing import Any, Dict, List, Optional, TypeAlias

# Определение Type Alias для улучшения читаемости
ItemType: TypeAlias = Dict[str, Any]
ItemListType: TypeAlias = List[ItemType]

data: ItemListType = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(data: ItemListType, state: Optional[str] = "EXECUTED") -> ItemListType:
    """Функция, которая принимает список словарей, опциональное значение для ключа state
    и возвращает новый список с указанным значением"""
    return [item for item in data if item.get("state") == state]


# Выход функции со статусом по умолчанию 'EXECUTED'
executed_items: ItemListType = filter_by_state(data)
print(executed_items)

# Выход функции, если вторым аргументом передано 'CANCELED'
canceled_items: ItemListType = filter_by_state(data, state="CANCELED")
print(canceled_items)


def sort_by_date(id_state_date: ItemListType, reverse: bool = True) -> ItemListType:
    """Функция, которая принимает список словарей с необязательным параметром
    и возвращает новый список, отсортированный по дате"""
    return sorted(id_state_date, key=lambda item: item["date"], reverse=reverse)


sorted_data: ItemListType = sort_by_date(data)
print(sorted_data)
