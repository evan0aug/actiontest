''' Use numpy for handling stats '''
import numpy as np 

STATS = [
    "STR",
    "DEX",
    "CON",
    "INT",
    "WIS",
    "CHA"
    ]


def generate_stats() -> np.ndarray:
    """ generate stats?"""
    for stat in STATS:
        stats = np.random.randint(1,7, (1,4))
        stats = np.delete(stats, stats.argmin())
        print(stat + ": " + str(stats) + ": " + str(stats.sum()))
    return stats

def main():
    """ Do something useful """
    generate_stats()


main()
