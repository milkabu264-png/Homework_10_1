from typing import List, Dict, Any


def filter_by_state(
    data: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    Параметры:
    data: Список словарей с данными
    state: Значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    Новый список с отфильтрованными словарями
    """
    result = []
    for item in data:
        if item["state"] == state:
            result.append(item)
    return result


def sort_by_date(
    data: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по дате.

    Параметры:
    data: Список словарей с данными
    reverse: Порядок сортировки (True - новые сначала, False - старые сначала)

    Возвращает:
    Новый отсортированный список
    """
    sorted_data = data.copy()
    sorted_data.sort(key=lambda x: x["date"], reverse=reverse)
    return sorted_data
