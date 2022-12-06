import numpy as np

from src.elements import Junction
from src.states import get_no_vehicles


class BasicScorer():
    @staticmethod
    def score(junction: Junction) -> float:
        lanes = np.array(
                        [connection.from_lane for connection in junction.connections])

        scores = dict()
        for phase in junction.phases:
            allowed_lanes = lanes[phase.allowed_indices]

            scores[phase.state] = 0
            # Use set() as the same lane might be used for 
            # multiple connections
            for lane in set(allowed_lanes):  
                scores[phase.state] += get_no_vehicles(lane)

        return scores
        