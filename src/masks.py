import re


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""
    card_number = re.sub(r"[^\d]", "", card_number)
    if len(card_number) != 16 or not card_number.isdigit():
        return ""
    masked_card_number = f"{card_number[:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    return masked_card_number


def main() -> None:
    card_number: str = input("Введите номер карты: ")
    masked_card_number: str = get_mask_card_number(card_number)
    if masked_card_number:
        print(masked_card_number)  # Выводим маскированный номер
    else:
        print("Неверный формат номера карты.")


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    account_number = re.sub(r"[^\d]", "", account_number)
    if len(account_number) != 16 or not account_number.isdigit():
        return ""
    masked_acc_number = f"****{account_number[-4:]}"
    return masked_acc_number


def main_account() -> None:
    account_number: str = input("Введите номер счета: ")
    masked_acc_number: str = get_mask_account(account_number)
    if masked_acc_number:
        print(masked_acc_number)
    else:
        print("Неверный формат номера счета.")


if __name__ == "__main__":
    main()
    main_account()
