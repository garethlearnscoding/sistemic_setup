from failsafe import failsafe
from djitellopy import tello

    
drone = tello.Tello()

@failsafe(drone)
def main():
    drone.connect()
    drone.takeoff()
    drone.set_video_direction(drone.CAMERA_FORWARD)
    drone.set_video_fps(drone.FPS_30)
    drone.stream_on()
    while True:
        drone.rotate_clockwise(180)




if __name__ == "__main__":
    main()


# Run the code and wait for the drone to start rotating
# Press key 'q' and see if the drone stops and land

# Run the code using: python test.py