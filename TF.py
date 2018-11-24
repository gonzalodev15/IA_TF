import numpy as np

from bayespy.nodes import Categorical, Mixture
from bayespy.inference import VB

FALSE = 0
TRUE = 1

def _or(p_false, p_true):
    return np.take([p_false, p_true], [[FALSE, TRUE], [TRUE, TRUE]], axis=0)

def Bayes(Enfermedades):
    BCandidiasica = Categorical([0.85, 0.15])
    BAnaerobios = Categorical([0.75, 0.25])
    BAerobios = Categorical([0.80,0.20])
    BHerpes = Categorical([0.7,0.3])
    BCircinada = Categorical([0.85,0.15])
    
    """Balanitis Candidiasica"""
    
    Erupciones = Mixture(BCandidiasica, Categorical,[[0.6,0.4],[0.1,0.9]])
    Dolor = Mixture(BCandidiasica, Categorical,[[0.75,0.25],[0.5,0.5]])
    Picor = Mixture(BCandidiasica, Categorical,[[0.55,0.45],[0.6,0.4]])
    Papulas  = Mixture(BCandidiasica, Categorical,[[0.75,0.25],[0.4,0.6]])
    Macula =  Mixture(BCandidiasica, Categorical,[[0.7,0.3],[0.45,0.55]])
    
    """Balanitis Anaerobios"""
    SurpuMaloliente = Mixture(BAnaerobios, Categorical,[[0.85,0.15],[0.55,0.45]])
    Edemas = Mixture(BAnaerobios, Categorical,[[0.85,0.15],[0.5,0.5]])
    Abdenitis = Mixture(BAnaerobios, Categorical,[[0.65,0.35],[0.60,0.40]])
    
    """Balanitis Aerobios"""
    Enrojecimiento = Mixture(BAerobios, Categorical,[[0.65,0.35],[0.6,0.4]])
    Fisuras = Mixture(BAerobios, Categorical,[[0.8,0.2],[0.4,0.6]])
    CEdemas = Mixture(BAerobios, Categorical,[[0.85,0.15],[0.65,0.35]])
    Eridmea = Mixture(BAerobios, Categorical,[[0.55,0.45],[0.7,0.3]])
    
    """Balanitis Herpes"""
    Vesiculas = Mixture(BHerpes, Categorical,[[0.6,0.4],[0.59,0.41]])
    UlDolorosas = Mixture(BHerpes, Categorical,[[0.85,0.15],[0.8,0.2]])
    CPapulas = Mixture(BHerpes, Categorical,[[0.6,0.4],[0.75,0.25]])
    InGangleos = Mixture(BHerpes, Categorical,[[0.6,0.4],[0.65,0.35]])
    
    """Balanitis Circinada"""
    LesBlancas = Mixture(BCircinada, Categorical,[[0.6,0.4],[0.70,0.30]])
    Artritis = Mixture(BCircinada, Categorical,[[0.65,0.35],[0.70,0.30]])
    Uretritis = Mixture(BCircinada, Categorical,[[0.55,0.45],[0.60,0.40]])
    Conjuntivitis = Mixture(BCircinada, Categorical,[[0.7,0.3],[0.75,0.25]])
    
    for x in Enfermedades:
        if x == "Erupciones":
            Erupciones.observe(TRUE)
            continue
        if x == "Dolor":
            Dolor.observe(TRUE)
            continue
        if x == "Picor":
            Picor.observe(TRUE)
            continue
        if x == "Macula":
            Macula.observe(TRUE)
            continue
        if x == "Supuracion maloliente":
            SurpuMaloliente.observe(TRUE)
            continue
        if x == "Abdenitis":
            Abdenitis.observe(TRUE)
            continue
        if x == "Fisuras":
            Fisuras.observe(TRUE)
            continue
        if x == "Eridmea":
            Eridmea.observe(TRUE)
            continue
        if x == "Vesiculas":
            Vesiculas.observe(TRUE)
            continue
        if x == "Ulceras dolorosas":
            UlDolorosas.observe(TRUE)
            continue
        if x == "Inflamacion de los gangleos":
            InGangleos.observe(TRUE)
            continue
        if x == "Lesiones blanco-grisaseas":
            LesBlancas.observe(TRUE)
            continue
        if x == "Artritis":
            Artritis.observe(TRUE)
            continue
        if x == "Uretritis":
            Uretritis.observe(TRUE)
            continue
        if x == "Conjuntivitis":
            Conjuntivitis.observe(TRUE)
            continue
        if x == "Papulas":
            Papulas.observe(TRUE)
            CPapulas.observe(TRUE)
            continue
        if x == "Edemas":
            Edemas.observe(TRUE)
            CEdemas.observe(TRUE)
            continue
        if x == "Enrojecimiento":
            Enrojecimiento.observe(TRUE)
    Q = VB(Conjuntivitis, Uretritis, Artritis, LesBlancas, InGangleos, UlDolorosas, Vesiculas, Eridmea, Fisuras, Enrojecimiento, Abdenitis, SurpuMaloliente,
      Macula,Picor,Dolor,Erupciones,BCircinada,BHerpes, BCandidiasica, BAnaerobios, BAerobios)
    Q.update(repeat=100)
    aux = f"Balanitis Candidiasica: {BCandidiasica.get_moments()[0][TRUE]}\nBalanitis Anaerobios: {BAnaerobios.get_moments()[0][TRUE]}\nBalanitis Aerobios: {BAerobios.get_moments()[0][TRUE]}\nBalanitis Herpes: {BHerpes.get_moments()[0][TRUE]}\nBalanitis Circinada:{BCircinada.get_moments()[0][TRUE]}"
    return aux
    
Juego = Bayes(['Dolor','Picor','Macula','Erupciones'])
print(Juego)