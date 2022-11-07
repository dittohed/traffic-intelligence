import os
import sys

import traci
from sumolib import checkBinary


if __name__ == '__main__':
    CFG_PATH = 'demo/sumo/cracow.sumocfg'
    USE_GUI = True

    os.environ['SUMO_HOME'] = '/usr/share/sumo/'
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
    sumo_binary = checkBinary('sumo-gui' if USE_GUI else 'sumo')
    traci.start([sumo_binary, '-c', CFG_PATH, '--start', '-d 1000'])

    for i in range(60):
        traci.simulationStep()
        print(f'Step: {i+1}, no. of vehicles: {traci.vehicle.getIDCount()}')

    traci.close()