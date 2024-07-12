def get_mask_card_number(card_number: str) -> str:
    """ "Функция, которая маскирует номер банковской карты"""
    card_number = card_number.replace(" ", "")
    masked_card_number = f"{card_number[:-16]} {card_number[-16:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    return masked_card_number


card_number: str = input("Введите номер карты: ")
masked_card_number: str = get_mask_card_number(card_number)
print(masked_card_number)


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    account_number = account_number.replace(" ", "")
    masked_account_number = "**" + account_number[-4:]
    return masked_account_number


account_number: str = input("Введите номер счета: ")
masked_acc_number: str = get_mask_account(account_number)
print(masked_acc_number)
