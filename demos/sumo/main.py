import os
import sys
import traci

from sumolib import checkBinary
from pathlib import Path

from src.scorer import BasicScorer
from src.elements import read_from_net_xml
from src.controller import BasicController


if __name__ == '__main__':
    CFG_PATH = 'demos/sumo/single_intersection.sumocfg'
    USE_GUI = True

    os.environ['SUMO_HOME'] = '/usr/share/sumo/'
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
    sumo_binary = checkBinary('sumo-gui' if USE_GUI else 'sumo')
    traci.start([sumo_binary, '-c', CFG_PATH, '--start', '-d 1000'])

    junctions = read_from_net_xml(Path('demos/sumo/single_intersection.net.xml'))
    junction = list(junctions.items())[0][1]

    for i in range(60):
        traci.simulationStep()
        print(f'Step: {i+1}, no. of vehicles: {traci.vehicle.getIDCount()}')
        scores = BasicScorer.score(junction)
        print(scores)
        BasicController.control(junction.id, scores)
        print('')

    traci.close()