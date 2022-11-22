from .q_learner import QLearner
from .coma_learner import COMALearner
from .qtran_learner import QLearner as QTranLearner
from .rode_learner import RODELearner
from .dmaq_qatten_learner import DMAQ_qattenLearner
from .latent_q_learner import LatentQLearner
from .sr_learner import SRLearner

REGISTRY = {}

REGISTRY["q_learner"] = QLearner
REGISTRY["coma_learner"] = COMALearner
REGISTRY["qtran_learner"] = QTranLearner
REGISTRY["rode_learner"] = RODELearner
REGISTRY["dmaq_qatten_learner"] = DMAQ_qattenLearner
REGISTRY["latent_q_learner"] = LatentQLearner
REGISTRY["sr_learner"] = SRLearner
