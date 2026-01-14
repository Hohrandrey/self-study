class TagList:
    def __init__(self, list_of_tags):
        self.list_of_tags = list_of_tags


    def __contains__(self, item):
        return item in self.list_of_tags

sp = []
for _ in range(5):
    i = input()
    sp.append(i)
taglist = TagList(sp[:3])
print(sp[3] in taglist)
print(sp[4] in taglist)
