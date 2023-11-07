# Over Under Robot PID Simulation
This simulation is used to test the effects of a Proportional Integral-Derivative (PID) Controller on our competition robot. 
The simulation is achieved by:
1. Running the PID and the simulation asynchronously on separate threads.
2. Updating the robot's position by a velocity and direction initialized on startup.
3. Treating the robot as having unique speeds for both sides (**left_speed** and **right_speed**), which are compared to obtain an offset angle.
4. Simulating error on these unique speeds.

The PID acts by taking the cross-track-error of the robot (the displacement of the robot perpendicular to the intended path), and applying a control method of the sum of three terms. For now, this simulation utilizes only the Proportional and Derivative terms of the controller, until the Integral term is found necessary. Therefore, the formula used in this simulation is as follows:
> Feedback = [ K_P * E(0) ] + { K_D * [ E(0) - E(-1) ] / t }

Where,
- E(0) is the Cross-Track Error
- E(-1) is the Previous Cross-Track Error
- t is the Time Interval
- K_P is the Proportional Constant
- K_D is the Derivative Constant

***Status update 11/06/2023***
<br>
*Full left_speed/right_speed integration is incomplete. This will be finished alongside moving from constant, repetitive, error addition to constant, uniform, and random error entry.*

## Setup
In order to install all the dependencies needed for this application, run 
`pip install -r requirements.txt` (in this directory). This can be done with or without a virtual environment (venv).

## Usage
To run this program, run `python main.py` in this directory. 
A window will be presented that represents a small (800x800) section of the virtual field for the simulated robot. Although it always stays on the window, its actual position can lie beyond the borders. The following keys have specific actions:
* **Left Arrow** rotates the robot 5 degrees to the left.
* **Right Arrow** rotates the robot 5 degrees to the right.
* **Space Bar** pauses the simulation.