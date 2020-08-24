import numpy as np


class EditDistinct():
    def __init__(self):
        self.distinct = 0
        self.table = None

    def init_table(self, str1, str2):
        self.table = np.zeros((len(str1), len(str2)))

    def __minimize(self, a, b=9999, c=9999):
        arr = np.array([a, b, c], dtype="int64")
        return min(arr)

    def start(self, str1, str2):
        str1 = " " + str1
        str2 = " " + str2
        self.init_table(str1, str2)
        return int(self.evaluate(str1, str2))

    def evaluate(self, str1, str2):
        for str1_pos in range(len(str1)):
            for str2_pos in range(len(str2)):
                if str1_pos == 0 and str2_pos != 0:
                    mini = self.__minimize(self.table[str1_pos][str2_pos - 1])
                elif str1_pos != 0 and str2_pos == 0:
                    mini = self.__minimize(self.table[str1_pos - 1][str2_pos])
                elif str1_pos == 0 and str2_pos == 0:
                    mini = 0
                else:
                    add = self.table[str1_pos][str2_pos - 1]
                    repl = self.table[str1_pos - 1][str2_pos - 1]
                    delete = self.table[str1_pos - 1][str2_pos]                
                    mini = self.__minimize(add, delete, repl)
                if str1[str1_pos] == str2[str2_pos]:
                    mini = self.table[str1_pos - 1][str2_pos - 1]
                if str1[str1_pos] != str2[str2_pos]:
                    mini += 1
                self.table[str1_pos][str2_pos] = mini
        return self.table[str1_pos][str2_pos]
        

ed = EditDistinct()

str1 = "聯式發票收銀機發票區聯式日"
str2 = "二聯式發票、收銀機發票(二聯式)"

print(ed.start(str1, str2))
