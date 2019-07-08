import numpy as np
import tkinter as tk

ALIVE = 1
DEAD = 0


"""
The judge_death method is:
Copyright (c) 2017 Maruyama Norihiro
Licensed under MIT
(https://github.com/alifelab/alife_book_src)
"""


class LifeGame(tk.Canvas):  # LifeGameConvとLifeGameShiftのテスト用
    def __init__(self, root, size=(50, 50), side_len=10,
                 ratio=0.5, sleep=50):
        self.height, self.width = size
        super().__init__(root, width=self.width*side_len,
                         height=self.height*side_len)
        self.state = np.random.binomial(1, ratio, size)
        self.side_len = side_len
        self.sleep = sleep
        self.pack()

    def judge_death(self):
        next_state = np.zeros((self.height, self.width), dtype=np.int8)
        for i in range(self.height):
            for j in range(self.width):
                # 自分と近傍のセルの状態を取得
                # c: center (自分自身)
                # nw: north west, ne: north east, c: center ...
                nw = self.state[i-1, j-1]
                n = self.state[i-1, j]
                ne = self.state[i-1, (j+1) % self.width]
                w = self.state[i, j-1]
                c = self.state[i, j]
                e = self.state[i, (j+1) % self.width]
                sw = self.state[(i+1) % self.height, j-1]
                s = self.state[(i+1) % self.height, j]
                se = self.state[(i+1) % self.height, (j+1) % self.width]
                neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
                if c == 0 and neighbor_cell_sum == 3:
                    next_state[i, j] = 1
                elif c == 1 and neighbor_cell_sum in (2, 3):
                    next_state[i, j] = 1
                else:
                    next_state[i, j] = 0
        self.state = next_state

    def draw_canvas(self):
        self.delete("all")
        row, column = np.where(self.state == ALIVE)
        x = column * self.side_len
        y = row * self.side_len
        create_square = np.frompyfunc(self.create_rectangle, 4, 1)
        create_square(x, y, x+self.side_len, y+self.side_len)

    def loop(self):
        self.draw_canvas()
        self.judge_death()
        self.after(self.sleep, self.loop)


if __name__ == '__main__':
    root = tk.Tk()
    game = LifeGame(root, size=(100, 100), side_len=5, sleep=20)
    game.loop()
    root.mainloop()
