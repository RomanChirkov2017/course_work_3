import pytest


@pytest.fixture
def jsons():
    return {
        "id": 619287771,
        "state": "EXECUTED",
        "date": "2019-08-19T16:30:41.967497",
        "operationAmount": {
            "amount": "81150.87",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 17691325653939384901",
        "to": "Счет 49304996510329747621"
    }
