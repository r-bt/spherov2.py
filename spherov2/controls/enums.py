from enum import Enum, auto


class RawMotorModes(Enum):
    OFF = auto()
    FORWARD = auto()
    REVERSE = auto()
    BREAK = auto()
    IGNORE = auto()


class PacketDecodingException(Exception):
    ...


class CommandExecuteError(Exception):
    ...