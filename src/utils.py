import os
import json
from config import ROOT_DIR

operations_path = os.path.join(ROOT_DIR, "src", "operations.json")


def get_all_operations(path):
    """Функция получает все операции по счетам"""
    with open(path, encoding='utf-8') as file:
        content = json.load(file)
    return content


# all_operationss = get_all_operations(operations_path)
# print(len(all_operationss))
# all_operations = get_all_operations(operations_path)
def get_executed_only(all_operations):
    """Функция получает ТОЛЬКО успешно-выполненные операции"""
    executed_list = []
    for operation in all_operations:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)
        else:
            continue
    return executed_list


# a = get_executed_only()
# print(a)
# executed_only =get_executed_only(all_operations)
def get_sorted_list(executed_only):
    """Функция сортирует операции, полученные в предыдущей функции, по дате """
    sorted_list = sorted(executed_only, key=lambda operation: operation["date"], reverse=True)
    return sorted_list


# b = get_sorted_list(executed_only)
# print(b)
def get_formated_date(data):
    """Функция преобразует дату в формат ДД.ММ.ГГГГ"""
    date = data[0:10]
    date.split('-')
    my_date = ".".join(reversed(date.split('-')))
    return my_date


def hide_requisites(requisites):
    """Функция маскирует номера карт и счетов"""
    parts = requisites.split()
    number = parts[-1]
    if requisites.lower().startswith('счет'):
        hided_number = f"**{number[-4:]}"
    else:
        hided_number = f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
    parts[-1] = hided_number

    return " ".join(parts)


def get_formated_operation(operation):
    """Функция выводит информацию по операции в нужном формате"""
    formated_date = get_formated_date(operation['date'])
    type_operation = operation['description']
    one_line_output = f"{formated_date} {type_operation}"

    if operation.get('from'):
        hided_from = hide_requisites(operation.get('from'))
    else:
        hided_from = 'Внесли наличные'
    hided_to = hide_requisites(operation.get('to'))
    two_line_output = f"{hided_from} -> {hided_to}"

    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']
    three_line_output = f"{amount} {currency}"

    return f"{one_line_output}\n{two_line_output}\n{three_line_output}\n"
