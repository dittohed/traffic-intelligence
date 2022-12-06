import traci

class BasicController():
    @staticmethod
    def control(junction_id: str, scores: dict):
        max_score_phase = max(scores, key=lambda x: scores[x])
        print(f'Switching to {max_score_phase}')

        traci.trafficlight.setRedYellowGreenState(junction_id, max_score_phase)
        