import Task_1
from main import current_list


def test_first_task():
    assert Task_1.creat_list_from_apple([]) == []


def test_first_task_2():
    assert Task_1.creat_list_from_apple(current_list) == ["Apple iPhone 13", "Apple iPhone 11", "Смартфон Apple iPhone 13 Pro"]