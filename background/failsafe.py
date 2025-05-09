import keyboard
from djitellopy import tello


def failsafe(Tello):
    keyboard.add_hotkey("q",lambda: keyboard.send("ctrl + c"))
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyboardInterrupt:
                print("\n[FAILSAFE] Executing failsafe handler...")
                emergency_landing(Tello)
        return wrapper
    return decorator



def emergency_landing(Tello):
    print("\n[FAILSAFE ACTIVATED] Force landing drone and exiting...")
    Tello.land()