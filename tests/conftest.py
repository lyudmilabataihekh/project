import pytest
from typing import Any, List, Dict
from io import StringIO
import sys

@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"date": "2022-01-01T12:00:00", "id": 1, "state": "EXECUTED"},
        {"date": "2022-01-02T12:00:00", "id": 2, "state": "EXECUTED"},
        {"date": "2022-01-01T12:00:00", "id": 3, "state": "EXECUTED"},
        {"date": "2021-12-31T12:00:00", "id": 4, "state": "EXECUTED"},
        {"date": "invalid date", "id": 5, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    ]


