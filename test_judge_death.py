import numpy as np
import tkinter as tk
import unittest

from lifegame import LifeGame
from lifegame_conv import LifeGameConv
from lifegame_shift import LifeGameShift


class TestJudgeDeath(unittest.TestCase):
    def test_lifegame_conv(self):
        root = tk.Tk()
        for _ in range(100):
            size = np.random.randint(1, high=100, size=2)
            lg = LifeGame(root, size=size)
            lg_conv = LifeGameConv(root, size=size)
            lg_conv.state = np.copy(lg.state)
            lg.judge_death()
            expected = lg.state
            lg_conv.judge_death()
            actual = lg_conv.state
            np.testing.assert_equal(actual, expected)

    def test_lifegame_shift(self):
        root = tk.Tk()
        for _ in range(100):
            size = np.random.randint(1, high=100, size=2)
            lg = LifeGame(root, size=size)
            lg_shift = LifeGameShift(root, size=size)
            lg_shift.state = np.copy(lg.state)
            lg.judge_death()
            expected = lg.state
            lg_shift.judge_death()
            actual = lg_shift.state
            np.testing.assert_equal(actual, expected)


if __name__ == "__main__":
    unittest.main()
