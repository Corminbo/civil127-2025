import os
from sokoban_controller import SokobanController

# use os.path.join for portable code (so it works on Mac/Windows/Linux)
path = os.path.join("/Users/tcormin/Desktop/Travail/EPFL/BA2/Programming and software development for engieers/civil127-2025/CIVIL-127/Exercise_4_2/Sokoban_files/levels"
                    , "/Users/tcormin/Desktop/Travail/EPFL/BA2/Programming and software development for engieers/civil127-2025/CIVIL-127/Exercise_4_2/Sokoban_files/levels/level1.xsb.txt")
sokoban = SokobanController(path)
sokoban.game_loop()

