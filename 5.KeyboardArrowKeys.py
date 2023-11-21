from spherov2 import scanner
from spherov2.sphero_edu import SpheroEduAPI
import keyboard
toy = scanner.find_toy()
def get_key():
    while True:
        return keyboard.read_event().name
   
def drive_with_keyboard(droid: SpheroEduAPI, speed_delta: int = 10, heading_delta: int = 30, dome_delta: int = 20):
    droid.set_speed(50)
    print('Press ESC key to exit...')  
    while True:
        key = get_key()
        if key == 'esc':
            return
        elif key == 'up':
            droid.set_speed(droid.get_speed() + speed_delta)
        elif key == 'down':
            droid.set_speed(droid.get_speed() - speed_delta)
        elif key == 'left':
            droid.set_heading(droid.get_heading() - heading_delta)
        elif key == 'right':
            droid.set_heading(droid.get_heading() + heading_delta)



with SpheroEduAPI(toy) as droid:
    drive_with_keyboard(droid)
