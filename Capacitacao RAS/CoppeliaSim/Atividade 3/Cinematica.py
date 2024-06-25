from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.getObject("sim")

# Handle do Carrim
handle_robo = sim.getObject('/Carrim')

# Handle dos motores
roda_direita = sim.getObject('/Carrim/rightMotor')
roda_esquerda = sim.getObject('/Carrim/leftMotor')

# Parametros do robô
L = 0.19
r = 0.0325

def calcular_velocidade(V, omega):
    omega_r = (2*V + omega * L) / (2*r)
    omega_l = (2*V - omega * L) / (2*r)
    return omega_r, omega_l

# Velocidades desejadas
v_desejada = 0.1 # Velocidade linear desejada
omega_desejada = 0.1 # Velocidade angular desejada

sim.startSimulation()

# Loop de controle
while sim.getSimulationTime() < 20:
    # Atualizar velocidades das rodas conforme necessário
    omega_r, omega_l = calcular_velocidade(v_desejada, omega_desejada)
    
    # Enviar comandos atualizados para as rodas
    sim.setJointTargetVelocity(roda_direita, omega_r)
    sim.setJointTargetVelocity(roda_esquerda, omega_l)



# definir a velocidade dos motores do Carrim
sim.setJointTargetVelocity(roda_direita, omega_r)
sim.setJointTargetVelocity(roda_esquerda, omega_l)

# Fechar a conexão com o CoppeliaSim

sim.stopSimulation()
