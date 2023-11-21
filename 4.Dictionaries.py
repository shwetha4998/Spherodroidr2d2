import math
import os
import sys
import threading
from datetime import datetime
from typing import List, Tuple, Iterator, Dict, Any
import time
import re
import cv2
import numpy
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from spherov2.types import Color
toy = scanner.find_toy()



color_names_to_rgb = {
    'black':Color(0,0,0),
    'white':Color(255,255,255),
    'red': Color(255, 0, 0),
    'lime':Color(0,255,0),
    'blue': Color(0, 0, 255),
    'yellow': Color(255, 255, 0),
    'cyan':Color(0,255,255),
    'magenta':Color(255,0,255),
    'silver':Color(192,192,192),
    'gray':Color(128,128,128),
    'maroon':Color(128,0,0),
    'olive':Color(128,128,0),
    'green':Color(0,128,0),
    'purple': Color(128, 0, 128),
    'teal': Color(0, 128, 128),
    'navy': Color(0, 0, 128),
    'indigo': Color(75, 0, 130),
    'violet': Color(238, 130, 238)
}

def set_lights(droid: SpheroEduAPI, color: str, which_light='both'):
    
    def hex2rgb(hex_code: str) -> Color:
        """convert HEX to RGB, one line"""
        return Color(*(int(hex_code[i:i+2], 16) for i in (0, 2, 4)))

    if re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
        color_rgb = hex2rgb(color)
    elif color in color_names_to_rgb:
        color_rgb = color_names_to_rgb[color]
    else:
        raise ValueError(f"Unknown color {color}")

    if which_light in ('front', 'both'):
        droid.set_front_led(color_rgb)
    if which_light in ('back', 'both'):
        droid.set_back_led(color_rgb)
with SpheroEduAPI(toy) as droid:
    set_lights(droid,'cyan','both')