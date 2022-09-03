# Author:  Lisandro Dalcin
# Contact: dalcinl@gmail.com
"""Execute computations asynchronously using MPI processes."""
# pylint: disable=redefined-builtin

import  logging

logging.basicConfig(level=logging.DEBUG, format="%(process)d:%(filename)s:%(lineno)d:%(message)s")

logging.debug("Logging mpi4py.futures")

from ._core import (
    Future,
    Executor,
    wait,
    FIRST_COMPLETED,
    FIRST_EXCEPTION,
    ALL_COMPLETED,
    as_completed,
    CancelledError,
    TimeoutError,
    InvalidStateError,
    BrokenExecutor,
)

from .pool import MPIPoolExecutor
from .pool import MPICommExecutor

from .pool import ThreadPoolExecutor
from .pool import ProcessPoolExecutor
