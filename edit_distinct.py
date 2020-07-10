import numpy as np


class EditDistinct():
    def __init__(self):
        self.table = None

    def __init_table(self, target: str, compared: str) -> None:
        '''
        if you want to get table\n
        you need to call this function before you calculate\n
        put strings that you want to comapred to init
        '''
        self.table = np.zeros((len(target)+1, len(compared)+1))

    def __minimize(self, a: int, b: int, c: int) -> int:
        arr = np.array([a, b, c], dtype="int64")
        return min(arr)

    def get_table(self) -> np.array:
        '''
        return the minimize table back
        '''
        return self.table

    def __calculate(self, target: str, compared: str, x: int, y: int) -> int:
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
                self.table[x][y] = self.__calculate(
                    target, compared, x - 1, y - 1)
            self.__calculate(target, compared, x - 1, y)
            self.__calculate(target, compared, x, y - 1)
            return self.__calculate(target, compared, x - 1, y - 1)
        else:
            if type(self.table) == np.ndarray:
                self.table[x][y] = self.__minimize(self.__calculate(target, compared, x - 1, y), self.__calculate(
                    target, compared, x, y - 1), self.__calculate(target, compared, x - 1, y - 1))+1
            return self.__minimize(self.__calculate(target, compared, x - 1, y), self.__calculate(target, compared, x, y - 1), self.__calculate(target, compared, x - 1, y - 1)) + 1
    
    def evaluate(self, target: str, compared: str) -> int:
        self.__init_table(target, compared)
        len1 = len(target)
        len2 = len(compared)
        return self.__calculate(target, compared, len1, len2)

def main():
    edit_distinct = EditDistinct()
    str1 = "cafe"
    str2 = "coffee"
    print(edit_distinct.evaluate(str1, str2))


if __name__ == "__main__":
    main()
