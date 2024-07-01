'''

from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.getObject("sim")

# Função de normalização dos ângulos ao intervalo [-pi, pi)
def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi

# Handle do Carrim
handle_robo = sim.getObject('/Carrim')

# Handle dos motores
roda_direita = sim.getObject('/Carrim/rightMotor')
roda_esquerda = sim.getObject('/Carrim/leftMotor')

# Parametros do robô
L = 0.19
r = 0.0325
maxv = 1.0
maxw = np.deg2rad(45)

# Definir o ponto do GOAL

handle_pPoint = sim.getObject('/Ponto_1')
goal_x, goal_y, goal_z = sim.getObjectPosition(handle_pPoint, -1)
goal_theta = sim.getObjectOrientation(handle_pPoint, -1)[2]


#rho inicia muito grande
rho = np.inf 


sim.startSimulation()

# Loop de controle
while rho > 0.05:

    # Obter posição e orientação atual do robô
    handle_robo = sim.getObject('/Carrim')
    x, y, z = sim.getObjectPosition(handle_robo, -1)
    theta = sim.getObjectOrientation(handle_robo, -1)[2]

    # Calculo do erro em x, y e theta

    current_pos = sim.getObjectPosition(handle_robo, -1)
    xd, yd, thetad = goal_x, goal_y, goal_theta

    e_x = xd - current_pos[0]
    e_y = yd - current_pos[1]
    e_theta = normalizeAngle(thetad - theta) 

    # Variaveis de estado atual (alpha, beta e rho) -> usar equações do slide
    rho = np.sqrt(e_x**2 + e_y**2)
    alpha = -theta + np.arctan2(e_y, e_x)
    beta = thetad - np.arctan2(e_y, e_x)

    alpha = normalizeAngle(alpha)
    beta = normalizeAngle(beta)

    # definir valores de constante proporcial

    kr = 4 / 20
    ka = 8 / 20
    kb = -1.5 / 20

    if np.abs(alpha) > np.pi/2:
        v = -kr * rho
    else:
        v = kr * rho

    w = ka * alpha + kb * beta

    # lembre-se de limitar as velocidades ao valor maximo do robo
    v = np.clip(v, -maxv, maxv)
    w = np.clip(w, -maxw, maxw)

    # calculo de WL e WR a partir de v e w
    WL = (v - L/2 * w) / r
    WR = (v + L/2 * w) / r

    # definir a velocidade dos motores do P3DX
    sim.setJointTargetVelocity(roda_direita, WR)
    sim.setJointTargetVelocity(roda_esquerda, WL)


# Parar o robô
sim.setJointTargetVelocity(roda_direita, 0)
sim.setJointTargetVelocity(roda_esquerda, 0)

# Finalizar simulação
sim.stopSimulation()


'''

from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import numpy as np

client = RemoteAPIClient()
sim = client.getObject("sim")

# Função de normalização dos ângulos ao intervalo [-pi, pi)
def normalizeAngle(angle):
    return np.mod(angle+np.pi, 2*np.pi) - np.pi

# Handle do Carrim
handle_robo = sim.getObject('/Carrim')

# Handle dos motores
roda_direita = sim.getObject('/Carrim/rightMotor')
roda_esquerda = sim.getObject('/Carrim/leftMotor')

# Parametros do robô
L = 0.19
r = 0.0325
maxv = 0.1
maxw = np.deg2rad(45)

# Define the goal point only once
handle_pPoint = sim.getObject('/Ponto_1')
goal_x, goal_y, goal_z = sim.getObjectPosition(handle_pPoint, -1)
goal_theta = sim.getObjectOrientation(handle_pPoint, -1)[2]

# rho inicia muito grande
rho = np.inf  

sim.startSimulation()

# Loop de controle
while rho > .2:
    # Obter posição e orientação atual do robô

    handle_robo=sim.getObject('/Carrim')
    x, y, z = sim.getObjectPosition(handle_robo, -1)
    theta = sim.getObjectOrientation(handle_robo, -1)[2]

    # calculo do erro em x, y e theta

    current_pos = sim.getObjectPosition(handle_robo, -1)
    xd, yd, thetad = goal_x, goal_y, goal_theta

    ex = xd - current_pos[0]
    ey = yd - current_pos[1]
    etheta = normalizeAngle(thetad - theta)

    # Variaveis de estado atual (alpha, beta e rho) -> usar equações do slide
    rho = np.sqrt(ex**2 + ey**2)
    alpha = -theta + np.arctan2(ey, ex)
    beta = thetad - np.arctan2(ey, ex)


    alpha = normalizeAngle(alpha)
    beta = normalizeAngle(beta)

    # definir valores de constante proporcial
    kr = 6 / 20
    ka = 7 / 20
    kb = 5 / 20

    if np.abs(alpha) > np.pi/2:
        v = -kr * rho
    else:
        v = kr * rho

    w = ka * alpha + kb * beta

    # lembre-se de limitar as velocidades ao valor maximo do robo
    v = np.clip(v, -maxv, maxv)
    w = np.clip(w, -maxw, maxw)

    # calculo de WL e WR a partir de v e w
    WL = (v - L/2 * w) / r
    WR = (v + L/2 * w) / r

    # definir a velocidade dos motores do P3DX
    sim.setJointTargetVelocity(roda_direita, WR)
    sim.setJointTargetVelocity(roda_esquerda, WL)

# Parar o robô
sim.setJointTargetVelocity(roda_direita, 0)
sim.setJointTargetVelocity(roda_esquerda, 0)

# Finalizar simulação
sim.stopSimulation()