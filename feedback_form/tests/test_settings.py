# flake8: noqa
"""Settings that need to be set in order to run the tests."""
import logging

from base_settings import *
from local_settings import *


logging.getLogger("factory").setLevel(logging.WARN)
