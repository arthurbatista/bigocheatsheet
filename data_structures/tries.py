class Node:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.end = False

class Tries:
    def __init__(self):
        self.root = {}

    def add(self, _str):
        current_level = self.root

        for i in range(len(_str)):
            if _str[i] not in current_level:
                current_level[_str[i]] = Node()

            current_level[_str[i]].count += 1

            if i+1 == len(_str):
                current_level[_str[i]].end = True

            current_level =  current_level[_str[i]].children

    def check_prefix(self, prefix):
        current_level = self.root

        for i in range(len(prefix)):
            if prefix[i] in current_level:
                if i+1 < len(prefix):
                    current_level =  current_level[prefix[i]].children
            else:
                print('Prefix NOT found!')
                return

        print('Prefix found!', current_level[prefix[-1]].count,
              current_level[prefix[-1]].end)


tries = Tries()
tries.add('arthuro')
tries.add('arthura')
tries.add('arthur')
tries.check_prefix('arthur')
