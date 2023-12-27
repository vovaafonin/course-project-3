import os
from src.utils import get_all_operations
from src.utils import get_executed_only
from src.utils import get_sorted_list
from src.utils import get_formated_date
from src.utils import hide_requisites
from src.utils import get_formated_operation
from config import ROOT_DIR


def test_get_all_operations():
    PATH_FOR_TEST = os.path.join(ROOT_DIR, "tests", "for_test.json")
    assert get_all_operations(PATH_FOR_TEST) == ["test"]

def test_get_executed_only():
    data = [{"id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689"},{"id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582"},{"id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093"}]
    expected = [{"id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582"},{"id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093"}]
    assert get_executed_only(data) == expected

def test_get_sorted_list():
    data = [{"date": "2018-09-12T21:27:25.241689"},
            {"date": "2019-12-08T22:46:21.935582"},
            {"date": "2018-04-04T17:33:34.701093"}]
    expected = [{"date": "2019-12-08T22:46:21.935582"},
            {"date": "2018-09-12T21:27:25.241689"},
            {"date": "2018-04-04T17:33:34.701093"}]
    assert get_sorted_list(data) == expected

def test_get_formated_date():
    data = "2018-04-04T17:33:34.701093"
    expected = "04.04.2018"
    assert get_formated_date(data) == expected

def test_hide_requisites():
    assert hide_requisites("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"
    assert hide_requisites("Счет 72731966109147704472") == "Счет **4472"

def test_get_formated_operation():
    operation_1 = {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }
    expected_1 = f"08.12.2019 Открытие вклада\nВнесли наличные -> Счет **5907\n41096.24 USD\n"

    operation_2 = {
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {
      "amount": "40701.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"
  }
    expected_2 = f"04.04.2018 Перевод организации\nVisa Gold 5999 41** **** 6353 -> Счет **4472\n40701.91 USD\n"
    assert get_formated_operation(operation_1) == expected_1
    assert get_formated_operation(operation_2) == expected_2