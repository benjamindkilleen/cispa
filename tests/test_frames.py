from cispa import FrameTransform
import numpy as np


def test_apply():
    F = FrameTransform(np.eye(3), np.zeros(3))
    v = np.array([1, 2, 3])
    assert np.allclose(F @ v, v)


def test_compose():
    F = FrameTransform(np.eye(3), np.zeros(3))
    G = FrameTransform(np.eye(3), np.zeros(3))
    assert np.allclose((F @ G).R, np.eye(3))
    assert np.allclose((F @ G).p, np.zeros(3))
    assert False
