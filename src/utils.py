import os
import json
from config import ROOT_DIR

operations_path = os.path.join(ROOT_DIR, "src", "operations.json")


def get_all_operations(path):
    with open(path, encoding='utf-8') as file:
        content = json.load(file)
    return content


#all_operationss = get_all_operations(operations_path)
#print(len(all_operationss))
def get_executed_only():
    all_operations = get_all_operations(operations_path)
    executed_list = []
    for operation in all_operations:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)
        else:
            continue
    return executed_list
#a = get_executed_only()
#print(a)
def get_sorted_list():
    executed_only =get_executed_only()
    sorted_list = sorted(executed_only, key=lambda operation: operation["date"], reverse=True)
    return sorted_list
#b = get_sorted_list()
#print(b)
