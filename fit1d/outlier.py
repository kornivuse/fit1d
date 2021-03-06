"""
This class is an abstract class that will be used for defining different types of
outliers removal handling.
"""

from abc import ABC, abstractmethod
from fit1d.model import Model
import numpy as np
from typing import Dict, List, Any, Callable


class OutLier(ABC):
    """
    The OutLier class contains the parameters for outlier and an abstract method
    to be implemented separately for each outliers removal function.
    """
    _outlier_parameters: Dict[str, Any] = dict()
    _fit: Callable
    _eval: Callable

    @abstractmethod
    def find_outliers(self, x: np.ndarray, y: np.ndarray, model: Model) -> List[int]:
        pass


class OutLierMock(OutLier):
    """ Mock class. Used only for tests. """
    DEFAULT_PARAMS = {'max error': 4, 'min points': 20}

    def __init__(self, outlier_parameters=DEFAULT_PARAMS, fit_func: Callable = None, eval_func: Callable = None):
        self._outlier_parameters = outlier_parameters
        self._fit = fit_func
        self._eval = eval_func

    def find_outliers(self, x: np.ndarray, y: np.ndarray, model: Model) -> List[int]:
        return [1, 2, 3]
