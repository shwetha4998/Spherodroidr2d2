 # Import the SpheroEduAPI class (replace with the actual import)
from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
from typing import Iterator
import time
# CIS 521: R2D2 - Homework 0
import math
import os
import sys
import threading
from datetime import datetime
from typing import List, Tuple, Iterator, Dict, Any

import cv2
import numpy
from spherov2.types import Color

toy = scanner.find_toy()


# Define Morse code mappings
def encode_in_morse_code(message: str) -> Iterator[str]:
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
    }

    for char in message:
        yield morse_code_dict[char.upper()]



def blink(droid: SpheroEduAPI, duration: float, intensity: int = 255):
    droid.set_holo_projector_led(True)
    time.sleep(1)
    droid.set_holo_projector_led(False)

def play_message(droid: SpheroEduAPI, message: str, dot_duration: float = 0.1, dash_duration: float = 0.3,
                 time_between_blips: float = 0.1, time_between_letters: float = 0.5):
    for morse_code in encode_in_morse_code(message):
        for char in morse_code:
            if char == '.':
                blink(droid, dot_duration)
                time.sleep(time_between_blips)
            else:
                blink(droid, dash_duration)
                time.sleep(time_between_blips)
        time.sleep(time_between_letters)


#if __name__ == '__main__':
with SpheroEduAPI(toy) as droid:
        play_message(droid, 'HELP')