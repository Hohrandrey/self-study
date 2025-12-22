from task import *


def validate_priority(x: str) -> int:
    match x:
        case "1":
            return 1
        case "2":
            return 2
        case "3":
            return 3
        case _:
            raise ValueError('Недопустимое значение')


def print_tasks(tasks: list[Task]) -> None:
    pass


def get_int(prompt: str) -> int:
    pass