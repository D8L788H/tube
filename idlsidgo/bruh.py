# Classes for managing the tubes
class TubeIterator:
    def __init__(self, tube):
        self.__tube = tube
        self.__index = 0

    def __next__(self):
        result = 'did not iterate'
        print(self.__tube.tubes)
        if self.__index < len(self.__tube.tubes):
            result = self.__tube.tubes[self.__index]
            self.__index += 1
            return result
        raise StopIteration


class Tube:
    # init methods only:
    def __init__(self, height, num):
        self.height = height
        self.num = num
        self.tubes = {}
        for y in range(self.num):
            tube = []
            for x in range(self.height):
                tube.append(' ')
            self.tubes.update({y: tube})

    def add(self, value, key):
        if self.tubes.get(key)[-1] != ' ':
            raise Exception
        else:
            for item in range(len(self.tubes.get(key))):
                if self.tubes.get(key)[item] == ' ':
                    self.tubes.get(key)[item] = value
                    break

    def move(self, start, end):
        lst_s = self.tubes.get(start)
        lst_e = self.tubes.get(end)
        lst_s_len = 0
        lst_e_len = 0
        value = []

        # get the length of list_s
        for item in lst_s:
            if item == ' ':
                lst_s_len = lst_s.index(item)
                break

        # get the values from the lst_s
        index_s = lst_s_len - 1
        value.append(lst_s[index_s])
        lst_s[index_s] = ' '
        while True:
            if lst_s[index_s - 1] == value[0]:
                value.append(lst_s[index_s - 1])
                lst_s[index_s - 1] = ' '
            elif lst_s[index_s - 1] != value[0]:
                break
            index_s -= 1

        # get the length of list_s
        for item in lst_e:
            if item == ' ':
                lst_e_len = lst_e.index(item)
                break

        # add the value to lst_e
        index_e = lst_e_len
        for item in value:
            lst_e[index_e] = item
            index_e += 1

    # output methods only:
    def __iter__(self):
        return TubeIterator(self)

    def pos(self, *position):
        # returns the value of the given key (can return multiple)
        out = []
        for times in range(len(position)):
            out.append(self.tubes.get(position[times]))
        return '\n'.join(str(x) for x in out)

    def __str__(self):
        out = '\n'.join(str(x) for x in self.tubes.values())
        return out
