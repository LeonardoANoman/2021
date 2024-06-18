"""
Antecedentes (entradas)

Serviço: que nota você daria para o serviço, em uma escala de 0 a 10?
ruim, aceitável, ótimo

Qualidade da comida: quão boa estava a comida, em uma escala de 0 a 10?
ruim, boa, saborosa

Consequentes (saídas)
Gorjeta: quanta gorjeta você daria, entre 0% e 20%?
baixa, média, alta

Regras

Se a qualidade da comida for ruim ou o serviço for ruim então a gorjeta será baixa
Se o serviço for médio então a gorjeta será média
Se o serviço for bom e a qualidade da comida for saborosa então a gorjeta será alta

"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Antecedentes e consequente

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), "qualidade")
servico = ctrl.Antecedent(np.arange(0, 11, 1), "servico")
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), "gorjeta")

# Membership functions

qualidade.automf(number=3,names=["ruim", "boa", "saborosa"])
servico.automf(number=3, names=["ruim", "aceitável", "ótimo"])

gorjeta["baixa"] = fuzz.trimf(gorjeta.universe, [0, 0, 10])
gorjeta["média"] = fuzz.trimf(gorjeta.universe, [0, 10, 20])
gorjeta["alta"] = fuzz.trimf(gorjeta.universe, [10, 20, 20])

regra1 = ctrl.Rule(qualidade["ruim"] | servico["ruim"], gorjeta["baixa"])
regra2 = ctrl.Rule(servico["aceitável"] , gorjeta["média"])
regra3 = ctrl.Rule(servico["ótimo"] | qualidade["saborosa"], gorjeta["alta"])

# Sistema de controle

sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])
sistema = ctrl.ControlSystemSimulation(sistema_controle)

sistema.input['qualidade'] = 8.6
sistema.input['servico'] = 6.5
sistema.compute()

print(sistema.output['gorjeta'])