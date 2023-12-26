from utils import get_all_operations
from utils import operations_path
from utils import get_executed_only
from utils import get_sorted_list
from utils import get_formated_operation

def main():
    all_operations = get_all_operations(operations_path)
    executed_only = get_executed_only(all_operations)
    sorted_list = get_sorted_list(executed_only)
    last_five_operations = sorted_list[0:5]
    for operation in last_five_operations:
        print(get_formated_operation(operation))


if __name__ == "__main__":
    main()
