# from __future__ import print_function
# from __future__ import division

import tensorflow as tf
import math
import numpy as np
import sys
import copy

from parallel_predictor import Predictor
from parallel_trajectory import Trajectory
from parallel_mppi import MPPI

STEP_LIMIT = 100
TIME_DURATION = 0.8
VELOCITY_SCALE = 0.03
STEP_ACTION = 0.03

def mppi_push(pos_x = 0.3, pos_y = 0.7, theta = math.pi):
    """ calculate the MPPI push to go toward the goal (pos_x, pos_y, theta). """

    mppi = MPPI(256, 3, STEP_ACTION)
    mppi.trajectory_set_goal(pos_x = float(pos_x),
            pos_y = float(pos_y),
            theta = float(theta))
    
    
    # mppi.U_reset()
    # mppi.trajectory_update_state(
    #         pose_object = np.array([0,0,0]),
    #         pose_tool=np.array([1,1,1])
        # )







def main():
    mppi_push(0.60, 0.60, 30.0)


if __name__ == "__main__":
    main()
