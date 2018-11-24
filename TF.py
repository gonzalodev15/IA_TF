import numpy as np

from bayespy.nodes import Categorical, Mixture
from bayespy.inference import VB

FALSE = 0
TRUE = 1

def _or(p_false, p_true):
    return np.take([p_false, p_true], [[FALSE, TRUE], [TRUE, TRUE]], axis=0)

BCandidiasica = Categorical([0.85, 0.15])
BAnaerobios = Categorical([0.75, 0.25])
BAerobios = Categorical([0.80,0.20])
BHerpes = Categorical([0.7,0.3])
BCircinada = Categorical([0.15,0.85])

Erupciones = Mixture(BCandidiasica, Categorical,[[0.6,0.4],[0.9,0.1]])
Dolor = Mixture(BCandidiasica, Categorical,[[0.75,0.25],[0.7,0.3]])
Picor = Mixture(BCandidiasica, Categorical,[[0.55,0.45],[0.6,0.4]])
Papulas  = Mixture(BCandidiasica, Categorical, BHerpes, Categorical,[0.6,0.4],[0.75,0.25])
Macula =  Mixture(BCandidiasica, Categorical,[[0.7,0.3],[0.8,0.2]])