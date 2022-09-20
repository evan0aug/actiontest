""" This a simple file for Evan to play with various tools without messing up Augment """

import sys
import time

import numpy as np

STATS = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]


def generate_stats() -> np.ndarray:
    """generate stats?"""
    for stat in STATS:
        stats = np.random.randint(1, 7, (1, 4))
        stats = np.delete(stats, stats.argmin())
        print(stat + ": " + str(stats) + ": " + str(stats.sum()))
    return stats


def main():
    """Do something useful"""
    generate_stats()


now = time.localtime()
print(now)
main()
sys.exit()
