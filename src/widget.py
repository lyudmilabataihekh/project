import re


def mask_account_card(card_data: str) -> str:
    """Функция, которая обрабатывает карты и счета"""
    card_data = card_data.replace(" ", "").replace("-", "")

    if "Счет" in card_data:
        # Проверка на учет счета
        account_number = card_data.replace("Счет", "").strip()
        if len(account_number) < 4 or not account_number.isdigit():
            return ""
            # Маска для счета
        masked_data_number = f"Счет ****{account_number[-4:]}"
        return masked_data_number

    else:
        # Проверка на номер карты
        if len(card_data) != 16 or not card_data.isdigit():
            return ""
            # Маска для карты
        masked_card_number = f"{card_data[:4]} {card_data[4:6]}** **** {card_data[-4:]}"
        return masked_card_number


def get_date(date: str) -> str:
    """Функция, которая меняет формат даты"""
    # Удаляем все, кроме цифр
    formated_date = re.sub(r"[^\d]", "", date)

    if len(formated_date) != 8:
        return ""

    year = formated_date[:4]
    month = formated_date[4:6]
    day = formated_date[6:8]

    modified_format = f"{day}.{month}.{year}"
    return modified_format


if __name__ == "__main__":
    card_data: str = input("Введите тип и номер карты или счета: ")
    masked_data_number: str = mask_account_card(card_data)
    print(masked_data_number)

    date: str = input("Введите дату: ")
    modified_format: str = get_date(date)
    print(modified_format)
