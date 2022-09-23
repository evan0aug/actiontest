"""This a simple file for Evan to play with various tools without messing up Augment."""
import sys
import time

import numpy as np

# TODO: allow user to arrange stats to rolled outcomes.
STATS = ["STR", "DEX", "CON",
"INT", "WIS", "CHA"]


def generate_stats() -> np.ndarray:
    """Generate stats and ennumerate through STATS."""
    for stat in STATS:
        stats = np.random.randint(1, 7, (1, 4))
        stats = np.delete(stats, stats.argmin())
        print(stat + ": " + str(stats) + ": " + str(stats.sum()))
    return stats


def main():
    """Do something useful. Seriously."""
    generate_stats()


main()
now = time.localtime()
print(now)
sys.exit()

print("Won't get here - will anything warn me?")
