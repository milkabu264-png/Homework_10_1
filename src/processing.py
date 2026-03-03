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

