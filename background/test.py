from djitellopy import tello
from failsafe import failsafe

drone = tello.Tello()


@failsafe(drone)
def main():
    drone.connect()# Connects to the drone
    drone.takeoff()# Tells the drone to Take off
    drone.set_video_direction(drone.CAMERA_FORWARD)
    drone.set_video_fps(drone.FPS_30)
    drone.stream_on()
    drone.move_up(20)# Tells the drone to Fly up
    while True:
        drone.rotate_clockwise(180)
    drone.land()



if __name__ == "__main__":
    main()

