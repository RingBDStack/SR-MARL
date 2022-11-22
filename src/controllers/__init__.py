REGISTRY = {}

from .basic_controller import BasicMAC
from .rode_controller import RODEMAC
from .separate_controller import SeparateMAC
from .sr_controller import SRMAC

REGISTRY["basic_mac"] = BasicMAC
REGISTRY['rode_mac'] = RODEMAC
REGISTRY["separate_mac"] =SeparateMAC
REGISTRY["sr_mac"] = SRMAC
