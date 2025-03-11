import os
import unittest
from sokoban_controller import SokobanController

class TestSokoban(unittest.TestCase):
    def test_level_completed(self):
        path = os.path.join("/Users/tcormin/Desktop/Travail/EPFL/BA2/Programming and software development for engieers/civil127-2025/CIVIL-127/Exercise_4_2/Sokoban_files/levels", "level1.xsb.txt")
        sokoban = SokobanController(path)
        # Simulate game state where all goals are covered by boxes
        sokoban.boxes = sokoban.goals.copy()
        self.assertTrue(sokoban.is_level_completed())

    def test_level_not_completed(self):
        path = os.path.join("/Users/tcormin/Desktop/Travail/EPFL/BA2/Programming and software development for engieers/civil127-2025/CIVIL-127/Exercise_4_2/Sokoban_files/levels", "level1.xsb.txt")
        sokoban = SokobanController(path)
        # Simulate game state where not all goals are covered by boxes
        sokoban.boxes = sokoban.goals[:-1]
        self.assertFalse(sokoban.is_level_completed())

if __name__ == '__main__':
    unittest.main()
