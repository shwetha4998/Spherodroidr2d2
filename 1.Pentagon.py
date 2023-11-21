from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
import time
from typing import List, Tuple, Iterator, Dict, Any
toy = scanner.find_toy()
def drive_with_commands(droid: SpheroEduAPI, roll_commands: List[Tuple[int, int, float]]):
    for command in roll_commands:
        heading, speed, duration = command
        droid.roll(heading,speed,duration)
with SpheroEduAPI(toy) as droid:
    # Pentagon Trajectory
    sort_lambda = lambda roll_commands: roll_commands.sort(key=lambda x: (x[1], x[0]))
    roll_commands = [(0, 100, 1), (72, 100, 1), (144, 100, 1), (288, 100, 1), (216, 100, 1)]
    sort_lambda(roll_commands)
    print(roll_commands)
    drive_with_commands(droid, roll_commands)
