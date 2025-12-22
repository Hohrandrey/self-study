import os
from task import *


def load_tasks(path: str) -> list[Task]:
    if not os.path.exists(path):
        return []
    else:
        return []



def save_tasks(path: str, tasks: list[Task]) -> None:
    pass