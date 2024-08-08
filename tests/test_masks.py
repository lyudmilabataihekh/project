import io
import sys

from unittest.mock import patch
import pytest

from src.masks import get_mask_account, get_mask_card_number, main, main_account


@pytest.mark.parametrize(
    "input_card, expected_output",
    [
        # Различные входные форматы
        ("7000792289606361", "7000 79** **** 6361"),
        ("70 00792289606 361", "7000 79** **** 6361"),
        ("7000-7922-8960-6361", "7000 79** **** 6361"),
        ("7000.7922.8960.6361", "7000 79** **** 6361"),  # Проверка альтернативного разделителя
        # Нестандартная длина
        ("7000", ""),
        ("7000 79", ""),
        ("7000 79 22", ""),
        ("", ""),
        # Неверные форматы
        ("abc", ""),
        ("1234 5678 9012 abcd", ""),
        ("12345678901234567", ""),  # Слишком длинный номер
        ("12345678901234", ""),
    ],
)
def test_get_mask_card_number(input_card: str, expected_output: str) -> None:
    assert get_mask_card_number(input_card) == expected_output


@pytest.mark.parametrize(
    "input_account, expected_output",
    [
        # Различные входные форматы
        ("1234567890123456", "****3456"),
        ("123 456 789 0123456", "****3456"),
        ("123-456-789-0123456", "****3456"),
        ("123.456.789.0123456", "****3456"),
        # Разные длины
        ("1234567890", ""),
        ("12345678", ""),
        ("1", ""),
        ("", ""),
        # Неверные форматы
        ("abc", ""),  # Буквы
        ("1234 5678 9012 abcd", ""),
        ("12345678901234567", ""),
        ("12a3456789", ""),
        ("12345678*", ""),
        ("1234567890.1234", ""),
    ],
)
def test_get_mask_account(input_account: str, expected_output: str) -> None:
    assert get_mask_account(input_account) == expected_output



def run_test(func, input_value, expected_output):
    with patch('builtins.input', return_value=input_value):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            func()  # Call the function being tested
            output = mock_stdout.getvalue()  # Capture the output
            assert output == expected_output  # Assert the expected output


def test_main():
    # Define test cases
    test_cases = [
        ("7000792289606361", "7000 79** **** 6361\n"),
        ("7000-7922-8960-6361", "7000 79** **** 6361\n"),
        ("abc", "Неверный формат номера карты.\n"),
    ]

    for input_card, expected_output in test_cases:
        run_test(main, input_card, expected_output)  # Run each test case


def test_main_account():
    # Define test cases
    test_cases = [
        ("1234567890123456", "****3456\n"),
        ("123 456 789 0123456", "****3456\n"),
        ("abc", "Неверный формат номера счета.\n"),
    ]

    for input_account, expected_output in test_cases:
        run_test(main_account, input_account, expected_output)  # Run each test case