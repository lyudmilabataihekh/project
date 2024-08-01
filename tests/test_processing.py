import pytest

data = [
    {'date': '2022-01-01T12:00:00', 'id': 1, 'state': 'EXECUTED'},
    {'date': '2022-01-02T12:00:00', 'id': 2, 'state': 'EXECUTED'},
    {'date': '2022-01-01T12:00:00', 'id': 3, 'state': 'EXECUTED'},
    {'date': '2021-12-31T12:00:00', 'id': 4, 'state': 'EXECUTED'},
    {'date': 'invalid date', 'id': 5, 'state': 'EXECUTED'},
    {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
    {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
]

def filter_by_state(data, state):
    """Фильтрация данных по статусу"""
    return [item for item in data if item['state'] == state]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [item for item in data if item['state'] == 'EXECUTED']),
    ("CANCELED", [item for item in data if item['state'] == 'CANCELED']),
    ("UNKNOWN_STATUS", []),
])
def test_filter_by_state(state, expected):
    """Тестирование фильтрации по статусам"""
    result = filter_by_state(data, state)
    assert result == expected
