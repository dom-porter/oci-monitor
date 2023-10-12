from enum import Enum, auto


class Providers(Enum):
    """ A list of supported IaaS providers """

    ORACLE = auto()
    AWS = auto()
