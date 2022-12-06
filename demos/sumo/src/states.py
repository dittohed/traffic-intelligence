import traci

def get_no_vehicles(lane: str):
    return traci.lane.getLastStepVehicleNumber(lane)