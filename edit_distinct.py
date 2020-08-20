import numpy as np


class EditDistinct():
    def __init__(self):
        self.max = 0
        self.min = 99999
    def __minimize(self, a, b, c):
        arr = np.array([a, b, c], dtype="int64")
        return min(arr)
    def start(self, s1, s2):
        self.max = len(s1) if len(s1) > len(s2) else len(s2)
        self.min = len(s1) if len(s1) > len(s2) else len(s2)
        self.evaluate(s1, s2)
        return self.min
    def evaluate(self, s1: str, s2: str, step: int = 0) -> int:
        '''
        s1, s2 => string\n
        will return these two string's Edit Distinct back
        '''
        if self.max < len(s1):
            self.max = len(s1)
        if self.max < len(s2):
            self.max = len(s2)

        if step >= self.min:
            return self.min
        
        print(s1, s2, step, self.min)
        if step >= self.max:
            return self.max
        if len(s1) == 0:
            step += len(s2)
            if self.min > step:
                self.min = step
            return step if step < self.max else self.max

        if len(s2) == 0:
            step += len(s1)
            if self.min > step:
                self.min = step
            return step if step < self.max else self.max

        if s1[0] == s2[0]:
            return self.evaluate(s1[1:], s2[1:], step)
            
        else:
            step += 1
            self.evaluate(s1[1:], s2[:], step)
            self.evaluate(s1[:], s2[1:], step)
            self.evaluate(s1[1:], s2[1:], step)

def main():
    edit_distinct = EditDistinct()    
    str1 = "聯式發票收銀機發票區聯式日"
    str2 = "二聯式發票、收銀機發票(二聯式)"
    print(edit_distinct.start(str1, str2))

if __name__ == "__main__":
    main()
