import numpy as np


class EditDistinct():
    def __init__(self):
        self.table = None

    def init_table(self, target, compared):
        '''
        if you want to get table\n
        you need to call this function before you evaluate\n
        put strings that you want to comapred to init
        '''
        self.table = np.zeros((len(target)+1, len(compared)+1))

    def __minimize(self, a, b, c):
        arr = np.array([a, b, c], dtype="int64")
        return min(arr)

    def get_table(self):
        '''
        return the minimize table back
        '''
        return self.table

    def evaluate(self, target, compared, x, y):
        '''
        target, compared => string\n
        x, y => len of target and len of compared\n
        will return these two string's Edit Distinct back
        '''
        if x == 0:
            if type(self.table) == np.ndarray:
                self.table[x][y] = y
            return y
        if y == 0:
            if type(self.table) == np.ndarray:
                self.table[x][y] = x
            return x

        if target[x - 1] == compared[y - 1]:
            if type(self.table) == np.ndarray:
                self.table[x][y] = self.evaluate(
                    target, compared, x - 1, y - 1)
            self.evaluate(target, compared, x - 1, y)
            self.evaluate(target, compared, x, y - 1)
            return self.evaluate(target, compared, x - 1, y - 1)
        else:
            if type(self.table) == np.ndarray:
                self.table[x][y] = self.__minimize(self.evaluate(target, compared, x - 1, y), self.evaluate(
                    target, compared, x, y - 1), self.evaluate(target, compared, x - 1, y - 1))+1
            return self.__minimize(self.evaluate(target, compared, x - 1, y), self.evaluate(target, compared, x, y - 1), self.evaluate(target, compared, x - 1, y - 1)) + 1


def main():
    edit_distinct = EditDistinct()
    str1 = "cafe"
    str2 = "coffee"
    print(edit_distinct.evaluate(str1, str2, len(str1), len(str2)))


if __name__ == "__main__":
    main()
