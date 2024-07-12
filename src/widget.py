def mask_account_card(card_data: str) -> str:
    """Функция, которая обрабатывает карты и счета"""
    if "Счет" in card_data:
        masked_data_number = (card_data[:4]) + (" **") + (card_data[-4:])
        return masked_data_number
    else:
        masked_data_number = f"{card_data[:-16]} {card_data[-16:-12]} {card_data[-12:-10]}** **** {card_data[-4:]}"
        return masked_data_number


card_data: str = input("Введите тип и номер карты или счета: ")
masked_data_number: str = mask_account_card(card_data)
print(masked_data_number)


def get_date(date: str) -> str:
    """Функция, которая меняет формат даты"""
    year = date[:4]
    month = date[5:7]
    day = date[8:10]

    modified_format = f"{day}.{month}.{year}"
    return modified_format


date: str = input("Введите дату: ")
modified_format: str = get_date(date)
print(modified_format)
