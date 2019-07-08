import numpy as np
import tkinter as tk

from lifegame import LifeGame


class LifeGameConv(LifeGame):
    def __init__(self, root, size=(50, 50), side_len=10,
                 ratio=0.5, sleep=50):
        super().__init__(root, size, side_len, ratio, sleep)

    def judge_death(self):
        states = self._processing()
        survival = np.sum(states, axis=(0, 1))
        self.state = (survival == 3) + self.state * (survival == 4)  # 生死判定

    def _processing(self):
        next_state = np.zeros((self.height+2, self.width+2), dtype=np.int8)
        next_state[1:-1, 1:-1] = self.state  # paddingの代わり
        next_state[self.height+1, 1:self.width+1] = self.state[0]
        next_state[0, 1:self.width+1] = self.state[self.height-1]
        next_state[-1, -1] = self.state[0, 0]
        next_state[0, 0] = self.state[-1, -1]
        next_state[1:-1, -1] = self.state[:, 0]
        next_state[1:-1, 0] = self.state[:, -1]
        next_state[0, -1] = self.state[-1, 0]
        next_state[-1, 0] = self.state[0, -1]
        return im2col(next_state, self.height+2, self.width+2, 3, 3)


"""
The im2col function is:
Copyright (c) 2016 Koki Saitoh
Licensed under MIT
(https://github.com/oreilly-japan/deep-learning-from-scratch/blob/master/LICENSE.md)
"""


def im2col(input_data, data_h, data_w, filter_h, filter_w):
    out_h = data_h - filter_h + 1
    out_w = data_w - filter_w + 1
    col = np.zeros((filter_h, filter_w, out_h, out_w))
    for y in range(filter_h):
        y_max = y + out_h
        for x in range(filter_w):
            x_max = x + out_w
            col[y, x, :, :] = input_data[y:y_max, x:x_max]
    return col


if __name__ == '__main__':
    root = tk.Tk()
    game = LifeGameConv(root, size=(100, 100), side_len=5, sleep=20)
    game.loop()
    root.mainloop()
