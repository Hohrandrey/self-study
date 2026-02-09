from typing import Protocol


class Playable(Protocol):
    def play(self):
        pass


class MusicTrack:
    def play(self, name):
        print(f'Играет трек: {name}')


class Video:
    def play(self, name):
        print(f"Воспроизводится видео: {name}")


def play_all(items: list[Playable]):
    MusicTrack().play(items[0])
    Video().play(items[1])


ls = [input(), input()]
play_all(ls)
