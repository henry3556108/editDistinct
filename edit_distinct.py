import numpy as np


class EditDistinct():
    def __init__(self):
        self.distinct = 0

    def __minimize(self, a, b, c):
        arr = np.array([a, b, c], dtype="int64")
        return min(arr)

    def evaluate(self, s1: str, s2: str, step: int = 0) -> int:
        '''
        s1, s2 => string\n
        will return these two string's Edit Distinct back
        '''
        if len(s1) == 0:
            step += len(s2)
            return step

        if len(s2) == 0:
            step += len(s1)
            return step

        if s1[0] == s2[0]:
            return self.evaluate(s1[1:], s2[1:], step)
        else:
            step += 1
            return self.__minimize(self.evaluate(s1[1:], s2[:], step),
                                   self.evaluate(s1[:], s2[1:], step),
                                   self.evaluate(s1[1:], s2[1:], step))

def main():
    edit_distinct = EditDistinct()
    str1 = "cafe"
    str2 = "coffee"
    print(edit_distinct.evaluate(str1, str2))


if __name__ == "__main__":
    main()
