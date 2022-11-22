REGISTRY = {}

from .rnn_agent import RNNAgent
from .rode_agent import RODEAgent
from .sr_agent import SRAgent
from .latent_ce_dis_rnn_agent import LatentCEDisRNNAgent
REGISTRY["rnn"] = RNNAgent
REGISTRY["rode"] = RODEAgent
REGISTRY["sr_agent"] = SRAgent
REGISTRY["latent_ce_dis_rnn"] = LatentCEDisRNNAgent
