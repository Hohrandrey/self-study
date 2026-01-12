class Playlist:
    def __init__(self):
        self.items = []


    def add(self, item):
        self.items.append(item)


    def __len__(self):
        return len(self.items)

playlist = Playlist()
for _ in range(3):
    i = input()
    playlist.add(i)
print(len(playlist))