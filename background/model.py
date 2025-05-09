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
    # Cammera streaming may require more code - need to test
    drone.move_up(10)# Tells the drone to Fly up
    drone.set_speed(25) # Set speeds to 25 cm/s
    for i in range(5): # Multiply forward distance by 5 [ 5m X 5 = 25m]
        drone.move_forward(500) # Tells the drone to move forward 500 cm [5 m]
    drone.land() # Tells the drone to land


if __name__ == "__main__":
    main()

