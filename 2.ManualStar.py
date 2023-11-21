import time
import math
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from typing import List, Tuple, Iterator, Dict, Any
toy = scanner.find_toy()
def drive_polygon(droid: SpheroEduAPI, n: int, speed: int = 100, duration: int = 1,a:bool=False):
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides")
   
    
    interior_angle=36
    exterior_angle= 180 -interior_angle
    def drive_with_commands(droid: SpheroEduAPI,roll_commands):
        for command in roll_commands:
            heading, speed, duration = command
            droid.roll(heading,speed,duration)

    for i in range(n):
        if a :
            roll_commands = [(round(i * interior_angle), speed, duration)]
            drive_with_commands(droid,roll_commands)
        else:
            roll_commands = [(round(i * exterior_angle), speed, duration)]
            drive_with_commands(droid,roll_commands)
with SpheroEduAPI(toy) as droid:
       drive_polygon(droid,5 ,100,1)   
