import math
import math
import os
import sys
import threading
from datetime import datetime
from typing import List, Tuple, Iterator, Dict, Any
import time
import time

import cv2
import numpy
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color# Assuming you're using Sphero SDK for controlling the robot

toy = scanner.find_toy()


def drive_pentagon(droid: SpheroEduAPI, n: int, speed: int = 50, duration: int = 2,a:bool=False):
    if n < 3:
        raise ValueError("A polygon must have at least 3 sides")
   
    interior_angle = (n - 2) * 180 / n
    #interior_angle=36
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
       drive_pentagon(droid,5 ,100,1)   


