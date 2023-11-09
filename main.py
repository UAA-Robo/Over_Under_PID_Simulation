from Application import *
from Logger import *
from PID import *
import time
import math
import threading as th
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    
    logger = Logger(["Cross Track Error", "Distance Traveled", "Heading Offset"])    

    def pid_correction():
        pid = PID()
        while simulation.isRunning:

            distance_y = simulation.pl.icebot.y_raw - simulation.pl.icebot.y_start
            distance_x = simulation.pl.icebot.x_raw - simulation.pl.icebot.x_start


            distance_from_start = math.sqrt((distance_x)**2 + (distance_y)**2)
            if distance_x != 0.0: 
                actual_angle = math.atan(distance_y / distance_x)
            else:
                actual_angle = math.radians(simulation.pl.icebot.angle_start)
            if distance_x < 0.0: actual_angle -= math.pi
            heading_offset = math.radians(simulation.pl.icebot.angle_start) - actual_angle
            pid.cross_track_error = distance_from_start * math.sin(heading_offset)
            # if not simulation.isPaused:
                # print("DATA_______________________________\n",
                #     f"Distance x: {distance_x} \n",
                #     f"Distance y: {distance_y} \n",
                #     f"Actual Angle: {actual_angle} \n",
                #     f"Heading Offset: {heading_offset} \n",
                #     f"X-Track Error: {pid.cross_track_error} \n", sep='', end='')
            # pid.cross_track_error += (simulation.pl.icebot.get_distance() *\
            #                         math.sin(math.radians(simulation.pl.icebot.intended_heading -\
            #                                                 simulation.pl.icebot.get_rotation())))
            logger.enter_data([pid.cross_track_error, distance_from_start, heading_offset])
            heading_correction = pid.correct_heading()
            simulation.pl.icebot.set_rotation(simulation.pl.icebot.get_rotation() + math.degrees(heading_correction))
            simulation.pl.icebot.reset_distance()
            time.sleep(0.020)


    simulation = Application("Over-Under Simulation", 800, 800)

    th1 = th.Thread(target=pid_correction)
    th1.start()
    while simulation.isRunning:
        simulation.tick()
        time.sleep(simulation.delay)
    logger.terminate()
    th1.join()
    

if __name__ == '__main__':
    main()
