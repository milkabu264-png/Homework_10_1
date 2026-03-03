def filter_by_state(data, state='EXECUTED'):
    """
    Фильтрует список словарей по значению ключа 'state'.

    Параметры:
    data (list): Список словарей с данными
    state (str): Значение для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    list: Новый список с отфильтрованными словарями
    """
    result = []
    for item in data:
        if item['state'] == state:
            result.append(item)
    return result


def sort_by_date(data, reverse=True):
    """
    Сортирует список словарей по дате.

    Параметры:
    data (list): Список словарей с данными
    reverse (bool):
        - True (по умолчанию) - сортировка по убыванию (сначала новые)
        - False - сортировка по возрастанию (сначала старые)

    Возвращает:
    list: Новый отсортированный список
    """
    # Копируем список, чтобы не изменять исходный
    sorted_data = data.copy()

    # Сортируем по ключу 'date'
    sorted_data.sort(key=lambda x: x['date'], reverse=reverse)

    return sorted_data