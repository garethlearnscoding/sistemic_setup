from background.failsafe import failsafe
from djitellopy import tello

    
drone = tello.Tello()

@failsafe(drone)
def main():
    ...




if __name__ == "__main__":
    main()