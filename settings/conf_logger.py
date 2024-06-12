"""Raid Logger configuration."""

import logging
from enum import Enum


class TypeLog(Enum):
    """."""

    debug = 0
    error = 1
    info = 2
    warning = 3
    critical = 4


class Log:
    """."""

    def __init__(self, name_call):
        """."""
        self.logs = logging.getLogger(name_call)
        self.logs.setLevel(logging.DEBUG)
        if not self.logs.handlers:
            stream_format = logging.Formatter(
                "RaidLog: time=%(asctime)s log_level=%(levelname)s "
                "ref=confronia ambient=DEV nivel=3 origin=%(name)s "
                "message=%(message)s",
                datefmt="%d/%m/%Y %H:%M:%S")
            stream = logging.StreamHandler()
            stream.setLevel(logging.DEBUG)
            stream.setLevel(logging.DEBUG)
            stream.setFormatter(stream_format)
            self.logs.addHandler(stream)

    def show_log(self, type_log, msg):
        """."""
        if type_log == 0:
            self.logs.debug(msg)
        elif type_log == 1:
            self.logs.error(msg)
        elif type_log == 2:
            self.logs.info(msg)
        elif type_log == 3:
            self.logs.warning(msg)
        elif type_log == 4:
            self.logs.critical(msg)
