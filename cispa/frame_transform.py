from __future__ import annotations
from typing import Union, overload
import numpy as np
from scipy.spatial.transform import Rotation


class FrameTransform:
    @property
    def R(self) -> np.ndarray:
        return self._R

    @R.setter
    def R(self, value: np.ndarray):
        if not isinstance(value, np.ndarray):
            raise TypeError(f"R must be a numpy.ndarray, not {type(value)}")
        if value.shape != (3, 3):
            raise ValueError(f"R must be a 3x3 matrix, not {value.shape}")

        d = np.linalg.det(value)
        if not np.isclose(d, 1.0):
            raise ValueError(f"R must be a rotation matrix, det(R) = {d}")

        self._R = value

    @property
    def p(self) -> np.ndarray:
        return self._p

    @p.setter
    def p(self, value: np.ndarray):
        if not isinstance(value, np.ndarray):
            raise TypeError(f"p must be a numpy.ndarray, not {type(value)}")
        if value.shape != (3,):
            raise ValueError(f"p must be a 3x1 vector, not {value.shape}")

        self._p = value

    def __init__(self, R: np.ndarray, p: np.ndarray):
        self.R = R
        self.p = p

    def __str__(self):
        return f"R = {self.R}\np = {self.p}"

    @overload
    def __matmul__(self, other: FrameTransform) -> FrameTransform:
        pass

    @overload
    def __matmul__(self, other: np.ndarray) -> np.ndarray:
        pass

    def __matmul__(self, other):
        if isinstance(other, FrameTransform):
            pass
        elif isinstance(other, np.ndarray):
            pass
        else:
            raise TypeError(f"Can't multiply FrameTransform with {type(other)}")

    def inverse(self) -> FrameTransform:
        pass

    @classmethod
    def from_matched_points(cls, X: np.ndarray, Y: np.ndarray):
        # Your implementation
        R = np.eye(3)
        p = np.zeros(3)

        return cls(R, p)
