import random
from os import system
from time import sleep

colors = ["\033[1;31m", "\033[33m", "\033[1;34m"]
love = "Vincent"

while True:
    i = random.randint(0, 2)
    print(
        colors[i],
        "\n".join(
            [
                "".join(
                    [
                        (
                            love[(x - y) % len(love)]
                            if (((x * 0.05) ** 2 
                                 + (y * 0.1) ** 2 - 1)
                                   ** 3
                            - (x * 0.05) ** 2 
                            * (y * 0.1) ** 3)
                            <= 0
                            else " "
                        )
                        for x in range(-30, 30)
                    ]
                )
                for y in range(15, -15, -1)
            ]
        ),
    )
    sleep(0.1)
    system("cls")