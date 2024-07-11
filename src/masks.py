from typing import Optional


def get_mask_card_number(card_number: Optional[str]) -> Optional[str]:
    """ "Функция, которая маскирует номер банковской карты"""
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        return "Неверное количество символов"
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_card_number


card_number: Optional[str] = input("Введите номер карты: ")
masked_card_number: Optional[str] = get_mask_card_number(card_number)
print(masked_card_number)


def get_mask_account(account_number: str) -> Optional[str]:
    """Функция, которая маскирует номер банковского счета"""
    account_number = account_number.replace(" ", "")
    masked_account_number = "**" + account_number[-4:]
    return masked_account_number


account_number: Optional[str] = input("Введите номер счета: ")
masked_acc_number: Optional[str] = get_mask_account(account_number)
print(masked_acc_number)
