import pytest
from src.processing import filter_by_state

test_cases = [
    ("EXECUTED", [1, 2, 3, 4, 5]),
    ("CANCELED", [594226727, 615064591]),
    ("UNKNOWN_STATUS", []),
]


@pytest.mark.parametrize("state, expected_ids", test_cases)
def test_filter_by_state(sample_data, state, expected_ids):
    # Получение результата на основе переданных `expected_ids`
    expected = [item for item in sample_data if item["id"] in expected_ids]

    result = filter_by_state(sample_data, state)
    assert result == expected