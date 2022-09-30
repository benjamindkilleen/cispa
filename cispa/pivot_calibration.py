import numpy as np
from typing import List, Tuple
import logging

from .frame_transform import FrameTransform


log = logging.getLogger(__name__)


def pivot_calibration(
    frames: List[FrameTransform], verbose: bool = False
) -> Tuple[np.ndarray, np.ndarray]:
    """Compute the pivot calibration of a robot arm.

    Args:
        frames: A list of FrameTransforms, each of which represents the
            transformation from the robot's base frame to the tool frame
            at a given time.
        verbose: If True, print the intermediate steps of the algorithm.


    Returns:
        A tuple of two numpy.ndarrays, representing the tip_in_tool and
        post_in_world transformations.
    """
    # Your implementation
    tip_in_tool = np.zeros(3)
    post_in_world = np.zeros(3)

    return tip_in_tool, post_in_world
