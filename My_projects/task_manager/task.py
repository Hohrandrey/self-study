class Task():
    def __init__(self, title: str, priority: int):
        self.title = title
        self.priority = priority


    def to_dict(self) -> dict:
        pass


    @staticmethod from_dict(d: dict) -> Task: