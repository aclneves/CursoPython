"""
CONSTANTE = "Variávies" que não vão mudar
Muitas condições no mesmo if(ruim)
    <- Contagem de complexidade (ruim), quanto mais tiver blocos de códigos
"""

velocidade = 65 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADAR = 60 # velocidade máxima do radar 1
LOCAL = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocida_carro_acima_radar = velocidade > RADAR
carro_multado_radar = local_carro >= (LOCAL - RADAR_RANGE) and local_carro <= (LOCAL + RADAR_RANGE)

if velocida_carro_acima_radar:
    print("Carro passou acima da velocidade no radar 1")

if carro_multado_radar and velocida_carro_acima_radar:
    print("Carro multado no radar")