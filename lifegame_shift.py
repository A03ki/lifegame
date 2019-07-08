import numpy as np
import tkinter as tk

from lifegame import LifeGame


class LifeGameShift(LifeGame):
    def __init__(self, root, size=(50, 50), side_len=10,
                 ratio=0.5, sleep=50):
        super().__init__(root, size, side_len, ratio, sleep)

    def judge_death(self):
        survival = self.count_life()
        self.state = (survival == 3) + self.state * (survival == 4)  # 生死判定

    def count_life(self):
        e = np.roll(self.state, -1, axis=1)  # 右
        w = np.roll(self.state, 1, axis=1)  # 左
        n = np.roll(self.state, 1, axis=0)  # 上
        s = np.roll(self.state, -1, axis=0)  # 下
        ne = np.roll(self.state, (1, -1), axis=(0, 1))  # 右上
        se = np.roll(self.state, (-1, -1), axis=(0, 1))  # 右下
        nw = np.roll(self.state, (1, 1), axis=(0, 1))  # 左上
        sw = np.roll(self.state, (-1, 1), axis=(0, 1))  # 左下
        return self.state + e + w + n + s + ne + se + nw + sw  # 9マスの生存数


if __name__ == '__main__':
    root = tk.Tk()
    game = LifeGameShift(root, size=(100, 100), side_len=5, sleep=20)
    game.loop()
    root.mainloop()
